"""Regenerate browser data, Georgian notes and the complete scene storyboard."""
from pathlib import Path
import ast,html,json,re
ROOT=Path(__file__).resolve().parent
def main():
    data=json.loads((ROOT/'lesson.json').read_text(encoding='utf-8'))
    tree=ast.parse((ROOT/'visual_scenes.py').read_text(encoding='utf-8'))
    titles=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='TITLES' for t in n.targets))
    compositions=re.findall(r'^\d{2}\. (.+)$',(ROOT/'design-notes.md').read_text(encoding='utf-8'),re.M)
    for i,s in enumerate(data):
        if titles[i]:s['title']=titles[i]
        s['visual']=compositions[i]
    data[22]['formula']='b: −2 → −1 → 0; შეცდომები: 1/6 → 0/6 → 0/6'
    additions={
        10:'ფორმალური ჩანაწერია T(u+v)=T(u)+T(v) და T(cu)=cT(u), ყველა u,v ვექტორისა და c რიცხვისთვის. ეს ორი პირობა განსაზღვრავს წრფივობას; კერძოდ T(0)=0.',
        14:'აქ ნაჩვენებია კონკრეტული საწინააღმდეგო მაგალითი. ეს არ ნიშნავს, რომ ნებისმიერი ორი მატრიცის რიგის შეცვლა ყოველთვის სხვადასხვა შედეგს იძლევა.',
        21:'ამ სპეციალურ მაგალითში W სიმეტრიულია, ამიტომ Wᵀ=W და ჩანაწერში რიცხვები არ იცვლება. ზოგადი მატრიცისთვის ტრანსპონირება ნამდვილად ცვლის სტრიქონებსა და სვეტებს.',
        23:'ნახატზე თეთრი წერტილი სწორი მნიშვნელობაა, ცისფერი — პროგნოზი. კვადრატების გვერდების შეფარდება 1:2-ია, ამიტომ ფართობების შეფარდება 1:4 გამოდის.',
        25:'პირველი დიდი ქსელი მხოლოდ სტრუქტურის სქემაა: ფერები და წრის შევსება გაზომილი ალბათობები არ არის. შემდეგ კადრზე ზუსტად გამოთვლილ 2→3 მაგალითზე გადავდივართ. გამოტოვებული კავშირების წონა ნულია; მწვანე კავშირია +1, წითელი −1.'}
    for i,n in additions.items():
        if n not in data[i]['notes']:data[i]['notes'].append(n)
    assert len(data)==30 and sum(s['seconds'] for s in data)==2700
    (ROOT/'lesson.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'lesson-data.js').write_text('const LESSON = '+json.dumps(data,ensure_ascii=False)+';\n',encoding='utf-8')
    e=html.escape
    css='''@font-face{font-family:Georgian;src:url(fonts/NotoSansGeorgian-Regular.ttf)}body{font:18px/1.85 Georgian,"Segoe UI",sans-serif;color:#17232c;background:white;max-width:940px;margin:40px auto;padding:0 30px}h1{font-size:32px;line-height:1.4}h2{font-size:25px;line-height:1.5}a{color:#086278}section{border-top:1px solid #b8c8ce;margin-top:36px;padding-top:20px}aside{padding:12px 20px;background:#edf4f5}.time{color:#086278}li{margin:8px 0}table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #ddd;padding:8px;text-align:left;font-size:16px}button{font:inherit;padding:10px 18px;cursor:pointer}.formula{font-family:Cambria,Georgian,serif;font-size:23px}@media print{body{font-size:11pt;line-height:1.5;margin:0}h1{font-size:22pt}h2{font-size:16pt}section{break-inside:avoid;margin-top:18pt}button{display:none}@page{size:A4;margin:18mm}}'''
    intro='<h1>წრფივი ალგებრა მანქანური სწავლებისთვის</h1><p>მომხსენებლის ჩანაწერები · ქართული · 30 სლაიდი · 45 წუთი</p><button onclick="window.print()">ბეჭდვა / PDF</button><p>→ ასრულებს მიმდინარე ანიმაციას და აჩერებს ბოლო კადრზე. შემდეგი → გადადის ახალ სლაიდზე. P — პაუზა; R — გამეორება; N — პირადი ჩანაწერები. დროის გეგმა მოიცავს ახსნას, მსჯელობასა და სავარჯიშოებს.</p><table><thead><tr><th>დრო</th><th>სლაიდი</th></tr></thead><tbody>'
    intro+=''.join(f'<tr><td>{s["start"]}–{s["end"]}</td><td><a href="#s{s["id"]}">{s["id"]:02}. {e(s["title"])}</a></td></tr>' for s in data)+'</tbody></table>'
    sections=[];md='# მომხსენებლის ჩანაწერები\n\nქართული · 30 სლაიდი · 45:00 · Manim Slides\n\n'
    plan='# Complete scene storyboard\n\nGeorgian live lesson; 30 scenes; 45:00 including discussion. Audience: high-school beginners with algebra and coordinate-graph knowledge; no previous vectors, matrices or ML.\n\nNarrative: measurable objects → vectors → combinations → transformations → scores → decisions → learning → networks. Three retrieval exercises precede their answer scenes.\n\n## Design and notation\n\nSee design-notes.md. Green = first component/basis or positive contribution; rose = second component/basis or negative contribution; cyan = input/data; yellow = result or boundary. Direct labels and category shapes provide redundant cues. The geometry is generated from coordinates, never approximated by artwork. Arrows/axes use a common unit on each plane.\n\n'
    for i,s in enumerate(data):
        notes=''.join(f'<p>{e(n)}</p>' for n in s['notes'])
        question=f'<aside><strong>კითხვა:</strong> {e(s["question"])}<br><strong>პასუხი:</strong> {e(s["answer"])}</aside>' if s['question'] else ''
        sections.append(f'<section id="s{s["id"]}"><p class="time">{s["start"]}–{s["end"]} · {s["seconds"]} წამი</p><h2>{s["id"]:02}. {e(s["title"])}</h2><p><strong>მიზანი:</strong> {e(s["purpose"])}</p><p class="formula">{e(s["formula"])}</p>{notes}{question}</section>')
        block=f'## {s["id"]:02}. {s["title"]}\n\n{s["start"]}–{s["end"]} · {s["seconds"]} წამი\n\n**მიზანი:** {s["purpose"]}\n\n**მათემატიკა:** {s["formula"]}\n\n'+'\n\n'.join(s['notes'])+'\n\n'
        if s['question']:block+=f'**კითხვა:** {s["question"]}\n\n**პასუხი:** {s["answer"]}\n\n'
        md+=block
        plan+=f'## {s["id"]:02}. {s["title"]}\n\n- Duration: {s["start"]}–{s["end"]} ({s["seconds"]} seconds).\n- Objective: {s["purpose"]}\n- Central insight: {s["title"]}\n- Mathematical content: {s["formula"]}\n- Composition, diagram and animation: {s["visual"]}\n- Exact construction: `visual_scenes.py`, `draw_{s["kind"]}()`; all coordinates, weights and transformation matrices are explicit.\n- Color semantics: the global system above; labels and matrix entries match their geometric components.\n- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.\n- Static alternative: `posters/{s["id"]:02}.jpg`.\n\n### Speaker notes\n\n'+'\n\n'.join(s['notes'])+'\n\n'
        if s['question']:plan+=f'**Audience task:** {s["question"]}\n\n**Expected answer:** {s["answer"]}\n\n'
        plan+=f'**Transition:** '+(f'Use this result to introduce “{data[i+1]["title"]}”. The next scene begins from its opening state, with no preview of its result.' if i<29 else 'Invite questions and the one-sentence exit answer from the notes.')+'\n\n'
    sources=[('3Blue1Brown — linear transformations','https://www.3blue1brown.com/lessons/linear-transformations/'),('3Blue1Brown — dot products','https://www.3blue1brown.com/lessons/dot-products/'),('3Blue1Brown — video source reference','https://github.com/3b1b/videos'),('Google — linear regression','https://developers.google.com/machine-learning/crash-course/linear-regression'),('Google — activation functions','https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions'),('Manim Slides','https://manim-slides.eertmans.be/latest/')]
    refs='<section><h2>წყაროები და შექმნა</h2><ul>'+''.join(f'<li><a href="{url}">{e(label)}</a></li>' for label,url in sources)+'</ul><p>ორიგინალური ანიმაციები: Manim Community 0.21.0 და Manim Slides 5.7.0. Noto Sans Georgian შრიფტი დართულია SIL Open Font License-ით. მათემატიკური ნიშნებისთვის გამოყენებულია Cambria. 3Blue1Brown-ის კოდი, ვიდეო და პერსონაჟები არ არის კოპირებული. ხილის მონაცემები გამოგონილია; სწავლა ნაჩვენებია სქემატურად.</p></section>'
    (ROOT/'speaker-notes.html').write_text(f'<!doctype html><html lang="ka"><head><meta charset="utf-8"><title>მომხსენებლის ჩანაწერები</title><style>{css}</style></head><body>{intro}'+''.join(sections)+refs+'</body></html>',encoding='utf-8')
    (ROOT/'speaker-notes.md').write_text(md,encoding='utf-8')
    (ROOT/'scenes.md').write_text(plan+'## References\n\n'+'\n'.join(f'- [{label}]({url})' for label,url in sources),encoding='utf-8')
    print('30 scene plans and Georgian notes generated; schedule = 45:00.')
if __name__=='__main__':main()
