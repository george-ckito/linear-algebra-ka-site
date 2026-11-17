"""Export the rendered Slide subclasses using Manim Slides' offline Reveal converter."""
from pathlib import Path
import subprocess,sys,json,argparse,os
import manim_slides
ROOT=Path(__file__).resolve().parent
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--count',type=int,default=30,help='Scene count for a preview export')
    parser.add_argument('--output',type=Path,default=ROOT/'index.html')
    args=parser.parse_args()
    # Manim Slides writes absolute media paths; make the source bundle relocatable.
    for path in [ROOT/'slides'/f'S{n:02}.json' for n in range(1,args.count+1)]:
        data=json.loads(path.read_text(encoding='utf-8'))
        for slide in data['slides']:
            for key in ('file','rev_file'):
                value=Path(slide[key])
                if value.is_absolute():slide[key]=value.relative_to(path.parent.parent).as_posix()
        path.write_text(json.dumps(data,ensure_ascii=True,indent=2),encoding='utf-8')
    template=(Path(manim_slides.__file__).parent/'templates'/'revealjs.html').read_text(encoding='utf-8')
    template=template.replace('<html>','<html lang="ka">').replace('</head>','<link rel="stylesheet" href="slides.css">\n</head>')
    template=template.replace('{% if loop.index == 1 and outer_loop.index == 1 %}\n          data-background-video-muted\n          {% endif %}','data-background-video-muted')
    ui='''
    <img id="loading-frame" alt="ანიმაციის საწყისი კადრი" src="openings/01.jpg">
    <div id="welcome"><p class="eyebrow">მანქანური სწავლების კლუბი · 45 წუთი</p>
    <h1>წრფივი ალგებრა<br>მანქანური სწავლებისთვის</h1>
    <p><strong>→ ანიმაციის დასრულება და გაჩერება</strong><br>შემდეგი → გადადის მომდევნო სლაიდზე.<br>← — წინა სლაიდის ბოლო კადრი · ხელახლა ← — გამეორება<br>N — მომხსენებლის ჩანაწერები · F — სრული ეკრანი · R — გამეორება</p>
    <button id="start">პრეზენტაციის დაწყება →</button></div>
    <nav id="toolbar" aria-label="პრეზენტაციის მართვა">
    <span id="position">01 / 30</span><select id="jump" aria-label="სლაიდის არჩევა"></select>
    <button id="back" aria-label="წინა სლაიდი">←</button><button id="forward">დასრულება →</button>
    <button id="pause">პაუზა P</button><button id="replay">გამეორება R</button>
    <button id="notes">ჩანაწერები N</button><button id="full">სრული ეკრანი F</button>
    </nav><p id="notice" role="status"></p>
    <script src="lesson-data.js"></script><script src="slides-controls.js"></script>
    '''
    # Insert after Reveal initialization; its asynchronous ready event then installs our controls.
    template=template.replace('</body>',ui+'\n</body>')
    target=ROOT/'manim-slides-template.html';target.write_text(template,encoding='utf-8')
    subprocess.run([sys.executable,'-m','manim_slides','convert',*[f'S{n:02}' for n in range(1,args.count+1)],str(args.output.resolve()),
        '--folder',str(ROOT/'slides'),'--offline','--use-template',str(target),
        '-ctitle=წრფივი ალგებრა — მანქანური სწავლების კლუბი','-ccontrols=false','-cprogress=false',
        '-ctransition=none','-cbackground_transition=none','-cauto_play_media=false','-ckeyboard=false'],check=True,cwd=ROOT,env={**os.environ,'PYTHONUTF8':'1'})
    print('Offline Manim Slides presentation exported.')
if __name__=='__main__':main()
