"""Render the lesson with a project virtual environment: python render.py [--qa] [--slides 1 2]."""
import argparse, os, sys, json
from pathlib import Path
from manim import tempconfig

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--qa',action='store_true',help='Render final frames and selected intermediate states only')
    parser.add_argument('--slides',type=int,nargs='+',default=list(range(1,31)))
    parser.add_argument('--height',type=int,default=1080)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    work=Path(os.environ.get('LESSON_WORK',str(root/'.render-cache')))
    cache=work/'manim-media'; cache.mkdir(parents=True,exist_ok=True)
    qa=work/'qa';qa.mkdir(parents=True,exist_ok=True)
    if args.qa:os.environ['LESSON_QA']=str(qa)
    else:os.environ.pop('LESSON_QA',None)
    import linear_algebra as lesson
    dest=root/'clips';dest.mkdir(exist_ok=True)
    for n in args.slides:
        if not 1<=n<=30:raise ValueError('Slide number must be 1–30')
        cfg=dict(media_dir=str(cache),video_dir=str(dest),images_dir=str(qa),
                 output_file=f'{n:02}',pixel_height=args.height,pixel_width=args.height*16//9,
                 frame_rate=30,frame_height=8,frame_width=128/9,
                 background_color=lesson.BG,disable_caching=True,
                 write_to_movie=not args.qa,save_last_frame=args.qa,
                 skip_animations=args.qa,verbosity='WARNING',progress_bar='none')
        print(f'Rendering {n:02}/30',flush=True)
        with tempconfig(cfg):
            options={} if args.qa else {'output_folder':root/'slides'}
            getattr(lesson,f'S{n:02}')(**options).render()
        if not args.qa:
            import av
            posters=root/'posters';posters.mkdir(exist_ok=True)
            openings=root/'openings';openings.mkdir(exist_ok=True)
            with av.open(str(dest/f'{n:02}.mp4')) as movie:
                last=None
                for frame in movie.decode(video=0):
                    if last is None:frame.to_image().save(openings/f'{n:02}.jpg',quality=92)
                    last=frame
                if last is not None:last.to_image().save(posters/f'{n:02}.jpg',quality=92)
    print('DONE',flush=True)
if __name__=='__main__':main()
