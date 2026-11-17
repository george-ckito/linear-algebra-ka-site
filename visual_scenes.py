"""Original ManimCE scenes for the redesigned Georgian visual lecture."""
from manim import *
from manim_slides import Slide
import numpy as np
import manimpango, json, os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
LESSON=json.loads((ROOT/'lesson.json').read_text(encoding='utf-8'))
manimpango.register_font(str(ROOT/'fonts'/'NotoSansGeorgian-Regular.ttf'))
BG='#06090C';INK='#F4F3EE';GRID='#1B4A5D';MUTED='#8B9BA5'
GREEN='#8DD78A';RED='#F17881';BLUE='#59C5E8';YELLOW='#F4DC6B'

def txt(s,size=32,color=INK,width=None):
    s=str(s);georgian=any('\u10a0'<=c<='\u10ff' for c in s)
    m=Text(s,font='Noto Sans Georgian' if georgian else 'Cambria',font_size=size,color=color,
           t2f={c:('Segoe UI' if georgian else 'Cambria Math') for c in set(s) if not ('\u10a0'<=c<='\u10ff') and not c.isspace()},line_spacing=.95)
    if width and m.width>width:m.scale_to_fit_width(width)
    return m
def at(s,xy,size=32,color=INK,width=None):return txt(s,size,color,width).move_to([*xy,0] if len(xy)==2 else xy)
def backed(m,pad=.13):return VGroup(BackgroundRectangle(m,color=BG,fill_opacity=.96,buff=pad,stroke_width=0),m).set_z_index(40)
def matrix(rows,colors=None,row_colors=None,size=44,dx=.85,dy=.8):
    cells=VGroup()
    for i,row in enumerate(rows):
        for j,v in enumerate(row):
            c=row_colors[i] if row_colors else (colors[j] if colors else INK)
            cells.add(at(str(v).replace('-','−'),[(j-(len(row)-1)/2)*dx,((len(rows)-1)/2-i)*dy],size,c))
    w=(len(rows[0])-1)*dx+.65;h=len(rows)*dy+.1
    brackets=VGroup(*[VMobject(color=INK,stroke_width=2).set_points_as_corners([[a*w/2,h/2,0],[a*(w/2+.16),h/2,0],[a*(w/2+.16),-h/2,0],[a*w/2,-h/2,0]]) for a in [-1,1]])
    result=VGroup(cells,brackets);result.cells=cells;return result
def mathrow(*parts,size=44,gap=.2):
    return VGroup(*[txt(p[0],size,p[1]) if isinstance(p,tuple) else (txt(p,size) if isinstance(p,str) else p) for p in parts]).arrange(RIGHT,buff=gap)
def fruit(pear=False,color=BLUE):
    points=([[-.07,.98,0],[-.32,.78,0],[-.36,.25,0],[-.68,-.25,0],[-.57,-.85,0],[0,-1,0],[.57,-.85,0],[.68,-.25,0],[.36,.25,0],[.32,.78,0],[.07,.98,0],[-.07,.98,0]] if pear else [[0,.72,0],[-.48,.9,0],[-.85,.48,0],[-.78,-.35,0],[-.43,-.86,0],[0,-.78,0],[.43,-.86,0],[.78,-.35,0],[.85,.48,0],[.48,.9,0],[0,.72,0]])
    body=VMobject(color=color,stroke_width=3,fill_color=color,fill_opacity=.17).set_points_smoothly(points)
    stem=ArcBetweenPoints([0,.8,0],[.12,1.25,0],angle=-.4,color=INK,stroke_width=3)
    leaf=Ellipse(width=.42,height=.18,color=GREEN,fill_opacity=.75,stroke_width=1).rotate(.4).move_to([.3,1.13,0])
    return VGroup(body,stem,leaf)

class Plane:
    def __init__(self,origin=(-3,-1.6),unit=1.15,bounds=(-7.12,7.12,-4,4),numbers=True):
        self.o=np.array([*origin,0.]);self.unit=unit;self.bounds=bounds
        l,r,b,t=bounds;lines=VGroup();labels=VGroup()
        for axis,low,high in [(0,l,r),(1,b,t)]:
            for k in np.arange(np.ceil((low-self.o[axis])/unit*2)/2,(high-self.o[axis])/unit+.01,.5):
                pos=self.o[axis]+k*unit;pts=([pos,b,0],[pos,t,0]) if axis==0 else ([l,pos,0],[r,pos,0])
                zero=abs(k)<.01;major=abs(k-round(k))<.01
                lines.add(Line(*pts,color=MUTED if zero else GRID,stroke_width=1.5 if zero else (.95 if major else .55),stroke_opacity=.85 if zero else (.68 if major else .28)))
                if numbers and major and not zero:
                    point=np.array([pos,self.o[1]-.25,0]) if axis==0 else np.array([self.o[0]-.25,pos,0])
                    if l+.3<point[0]<r-.3 and b+.35<point[1]<min(t-.3,2.8):labels.add(at(str(int(k)),point,18,MUTED))
        self.lines=lines.set_z_index(-20);self.labels=labels.set_z_index(-10)
    def p(self,x,y):return self.o+self.unit*np.array([x,y,0])
    def arrow(self,xy,color=YELLOW,start=(0,0),width=5):return Arrow(self.p(*start),self.p(*xy),buff=0,color=color,stroke_width=width,max_tip_length_to_length_ratio=.16).set_z_index(5)
    def poly(self,points,color=YELLOW,fill=.13):return Polygon(*[self.p(*p) for p in points],color=color,fill_opacity=fill,stroke_width=2).set_z_index(0)

TITLES=['','წესს მაგალითებიდან ვპოულობთ','რიცხვები აღწერს საგანს','ვექტორი აერთიანებს კოორდინატებს','შეკრება აერთიანებს გადაადგილებებს','რიცხვი ცვლის ვექტორის მასშტაბს','სად მიგვიყვანს ორი მიმართულება?','საბაზისო ვექტორები','ერთი მიმართულება მხოლოდ წრფეს ფარავს','მატრიცა გარდაქმნის ვექტორს','ერთი წესი მოქმედებს მთელ სიბრტყეზე','სვეტები გვიჩვენებს ახალ მიმართულებებს','სად აღმოჩნდება ეს ვექტორი?','პასუხს სვეტების კომბინაცია გვაძლევს','მოქმედებების რიგი ცვლის შედეგს','ორი ვექტორიდან ვიღებთ ერთ ქულას','პროექციას აქვს სიდიდე და ნიშანი','ქულა გვაძლევს კატეგორიას','ნულოვანი ქულა ქმნის საზღვარს','თავისუფალი წევრი წევს საზღვარს','მატრიცა ითვლის რამდენიმე ქულას','სტრიქონები სხვადასხვა მაგალითია','სწავლისას ვცვლით პარამეტრებს','შეცდომის კვადრატი ზომავს აცდენას','ახალი მაგალითები ამოწმებს წესს','ქსელის ფენა აერთიანებს წონიან ჯამებს','ReLU ნულავს უარყოფით მნიშვნელობებს','გამოიყენეთ ყველაფერი ერთად','საზღვრის გადაკვეთა ცვლის პასუხს','რიცხვებიდან პროგნოზამდე']
SlideBase = Scene if os.environ.get('LESSON_QA') else Slide
class Talk(SlideBase):
    number=1
    skip_reversing=True
    def setup(self):self.camera.background_color=ManimColor(BG);self.beats=0;self.data=LESSON[self.number-1]
    def construct(self):
        if isinstance(self,Slide):
            d=self.data
            notes=f"{d['id']:02}. {d['title']}\n\n{d['start']}–{d['end']} · {d['seconds']} წამი\n\n"+'\n\n'.join(d['notes'])
            if d['question']:notes+=f"\n\nკითხვა: {d['question']}\n\nპასუხი: {d['answer']}"
            self.next_slide(notes=notes)
        if self.number!=1:
            h=txt(TITLES[self.number-1],30,width=11.4).to_corner(UL,buff=.55)
            self.add(backed(h,.15),backed(at(f'{self.number:02}',[6.2,3.4],21,MUTED),.1))
        self.wait(.25)
        getattr(self,'draw_'+self.data['kind'])();self.beat();self.wait(1.5)
    def reveal(self,*m,run_time=.8):self.play(*[FadeIn(x) for x in m],run_time=run_time)
    def beat(self):
        self.wait(1.1);self.beats+=1
        if os.environ.get('LESSON_QA'):
            self.renderer.update_frame(self)
            self.camera.get_image().save(Path(os.environ['LESSON_QA'])/f'{self.number:02}-{self.beats:02}.png')
    def plane(self,**kwargs):
        p=Plane(**kwargs);self.add(p.lines,p.labels);return p
    def annotation(self,s,point,size=32,color=INK,width=None):return backed(at(s,point,size,color,width))
    def equation(self,m,point=(0,-2.9)):
        m.move_to([*point,0]);return backed(m,.2)
    def pulse(self,lines,color=YELLOW):self.play(*[ShowPassingFlash(l.copy().set_stroke(color,4),time_width=.35) for l in lines],run_time=1.4)
    def dot(self,p,xy,color=BLUE,r=.09):return Dot(p.p(*xy),radius=r,color=color).set_z_index(7)
    def endpoint(self,p,xy,text,color=YELLOW,direction=UR):return backed(txt(text,28,color).next_to(p.p(*xy),direction,buff=.15))

    def draw_cover(self):
        p=self.plane(origin=(2,-1.7),unit=1.15,numbers=False);p.lines.set_opacity(.35)
        title=VGroup(txt('წრფივი',64),txt('ალგებრა',64)).arrange(DOWN,aligned_edge=LEFT,buff=.15).move_to([-3.8,.6,0]);self.add(backed(title,.35))
        self.reveal(self.annotation('მანქანური სწავლებისთვის',[-3.7,-1.15],24,BLUE,width=5.7))
        e1=p.arrow((2,0),GREEN);e2=p.arrow((0,2),RED);area=p.poly([(0,0),(2,0),(2,2),(0,2)],YELLOW,.16)
        self.play(Create(area),GrowArrow(e1),GrowArrow(e2),run_time=2.2)
        self.play(VGroup(area,e1,e2).animate.apply_matrix([[1,.55],[.25,1]],about_point=p.o),run_time=3)
        self.reveal(self.annotation('45 წუთი · მანქანური სწავლების კლუბი',[-3.5,-2.6],19,MUTED,width=6))
    def draw_ml(self):
        p=self.plane(origin=(-3.4,-2),unit=1.05,numbers=False)
        a=[(.7,1),(1.5,.8),(1.2,1.8),(2.3,1.5),(2.8,1)];b=[(.6,3.4),(1.2,4),(2,3.5),(2.9,3.9),(3.3,3)]
        dots=VGroup(*[self.dot(p,v,GREEN,.12) for v in a],*[Triangle(color=RED,fill_opacity=1).scale(.14).move_to(p.p(*v)) for v in b])
        self.play(LaggedStart(*[GrowFromCenter(x) for x in dots],lag_ratio=.12),run_time=2.4)
        self.play(Create(Line(p.p(-1,2.4),p.p(5,2.4),color=YELLOW,stroke_width=3)),run_time=2)
        self.reveal(self.annotation('მაგალითები',[-4.9,2.2],28),self.annotation('სწორი პასუხებით',[-4.9,1.6],21,MUTED))
        q=self.dot(p,(4.8,1.4),INK,.17);mark=self.annotation('?',p.p(4.8,1.4)+UP*.55,46);self.reveal(q,mark);self.beat()
        self.play(q.animate.set_color(GREEN),Transform(mark,self.annotation('პროგნოზი',p.p(4.8,1.4)+UP*.65,25,GREEN)),run_time=1.4)
        self.reveal(self.annotation('წესი მაგალითებიდან',[3.1,-2.9],30,YELLOW,width=6))
    def draw_features(self):
        f=fruit(True,BLUE).scale(1.8).move_to([-3.1,-.15,0]);self.play(DrawBorderThenFill(f),run_time=2)
        self.play(GrowArrow(DoubleArrow([-4.4,-2.25,0],[-1.8,-2.25,0],buff=0,color=GREEN)),GrowArrow(DoubleArrow([-4.95,-1.9,0],[-4.95,1.55,0],buff=0,color=RED)),run_time=1.8)
        self.reveal(self.annotation('სიგანე  2',[-3.1,-2.85],29,GREEN),self.annotation('სიმაღლე  3',[-4.75,2.1],28,RED,width=3.2))
        m=matrix([[2],[3]],row_colors=[GREEN,RED],size=70,dy=1.25).move_to([2.6,.1,0]);self.play(TransformFromCopy(f,m),run_time=2)
        self.reveal(self.annotation('x =',[.9,.1],52),self.annotation('ერთი საგანი · ორი ნიშანი',[2.6,-2.4],26,MUTED,width=6))
    def draw_vector(self):
        p=self.plane(origin=(-3.8,-1.9),unit=1.3);a=p.arrow((2,0),GREEN);b=p.arrow((2,3),RED,start=(2,0))
        self.play(GrowArrow(a),run_time=1.5);self.play(GrowArrow(b),run_time=1.8)
        self.reveal(self.annotation('2',p.p(1,0)+DOWN*.4,38,GREEN),self.annotation('3',p.p(2,1.5)+RIGHT*.45,38,RED))
        self.play(GrowArrow(p.arrow((2,3))),run_time=2)
        self.reveal(self.endpoint(p,(2,3),'x',YELLOW),self.equation(mathrow('x =',matrix([[2],[3]],row_colors=[GREEN,RED],size=54)),(3.6,-.4)))
    def draw_addition(self):
        p=self.plane(origin=(-3.7,-1.9),unit=1.25);a=p.arrow((2,1),GREEN);b=p.arrow((1,2),RED)
        self.play(GrowArrow(a),GrowArrow(b),run_time=2);self.beat();self.add(b.copy().set_opacity(.22))
        self.play(Transform(b,p.arrow((3,3),RED,start=(2,1))),run_time=2.5);self.play(GrowArrow(p.arrow((3,3))),run_time=2)
        self.reveal(self.endpoint(p,(2,1),'u',GREEN,DOWN),self.endpoint(p,(3,3),'u + v',YELLOW))
        self.reveal(self.equation(mathrow(('(2, 1)',GREEN),'+',('(1, 2)',RED),'=',('(3, 3)',YELLOW),size=37),(2.9,-2.8)))
    def draw_scaling(self):
        p=self.plane(origin=(0,-.3),unit=1.15);a=p.arrow((1,1),BLUE);self.play(GrowArrow(a),run_time=1.4);self.add(a.copy().set_opacity(.25))
        caption=self.annotation('1 · v',[-4.4,1.5],56,BLUE);self.reveal(caption)
        for k,c in [(2,GREEN),(.5,BLUE),(-1,RED)]:
            self.play(Transform(a,p.arrow((k,k),c)),Transform(caption,self.annotation(f'{str(k).replace("-","−")} · v',[-4.4,1.5],56,c)),run_time=2.5);self.beat()
        self.reveal(self.annotation('v = (1, 1)',[4.1,2],35,BLUE),self.annotation('−v = (−1, −1)',[3.8,-2.7],38,RED))
    def basis(self,p):
        a=p.arrow((1,0),GREEN);b=p.arrow((0,1),RED);self.play(GrowArrow(a),GrowArrow(b),run_time=1.7)
        self.basis_labels=VGroup(self.endpoint(p,(1,0),'e₁',GREEN,DOWN),self.endpoint(p,(0,1),'e₂',RED,LEFT))
        self.reveal(self.basis_labels);return a,b
    def draw_exercise(self):
        p=self.plane(origin=(-3.3,-1.5),unit=1.25);self.basis(p)
        self.reveal(self.equation(mathrow(('2e₁',GREEN),'+',('3e₂',RED),'= ?',size=62),(2.7,1.4)))
        self.reveal(self.annotation('დახატეთ საბოლოო ისარი',[2.7,-.2],29,width=6),self.annotation('40 წამი ფიქრისთვის',[2.7,-1],22,MUTED))
    def draw_basis(self):
        p=self.plane(origin=(-3.6,-1.9),unit=1.2)
        steps=[p.arrow((i+1,0),GREEN,start=(i,0)) for i in range(2)]+[p.arrow((2,j+1),RED,start=(2,j)) for j in range(3)]
        self.play(LaggedStart(*[GrowArrow(a) for a in steps],lag_ratio=.45),run_time=4);self.play(GrowArrow(p.arrow((2,3))),run_time=2)
        self.reveal(self.annotation('საბაზისო ვექტორები',[3.35,2.45],27,MUTED,width=5.4),
                    self.endpoint(p,(1,0),'e₁',GREEN,DOWN),self.endpoint(p,(2,1),'e₂',RED,RIGHT))
        self.reveal(self.equation(mathrow(('2e₁',GREEN),'+',('3e₂',RED),size=48),(3.4,1.2)),self.equation(mathrow('=',matrix([[2],[3]],row_colors=[GREEN,RED],size=56)),(3.4,-.7)))
    def draw_span(self):
        p=self.plane(origin=(-1,-.4),unit=.95)
        self.play(Create(Line(p.p(-3.2,-3.2),p.p(3.6,3.6),color=BLUE,stroke_width=2)),run_time=2)
        self.play(LaggedStart(*[GrowFromCenter(self.dot(p,(k,k),BLUE,.08)) for k in [-3,-2,-1,1,2,3]],lag_ratio=.2),run_time=2)
        a=p.arrow((1,1),GREEN);self.play(GrowArrow(a));self.play(Transform(a,p.arrow((2,2),GREEN)),run_time=2)
        self.reveal(self.dot(p,(2,1),RED,.12),self.endpoint(p,(2,1),'(2, 1)',RED,RIGHT))
        self.reveal(self.annotation('a(1, 1)',[-4.3,1.7],49,BLUE),self.annotation('ერთი წრფე',[-4.3,.65],30),self.annotation('მეორე მიმართულება გვჭირდება',[2.6,-2.8],27,RED,width=7))
    def stretch_scene(self,comparison=False):
        if comparison:
            p=self.plane(origin=(-4.1,-.4),unit=.83,bounds=(-6.5,-.45,-2.8,2.5),numbers=False)
            q=self.plane(origin=(2.7,-.4),unit=.83,bounds=(.45,6.5,-2.8,2.5),numbers=False)
            shape=[(-1,-1),(1,-1),(1,1),(-1,1)];left=p.poly(shape,YELLOW,.2);right=q.poly(shape,YELLOW,.2)
            dots=VGroup(*[self.dot(q,xy,BLUE) for xy in [(-1,1),(1,1),(.5,-.5)]]);self.reveal(left,right,dots)
            self.add(q.lines.copy().set_opacity(.25))
            target=q.lines.copy().apply_matrix([[2,0],[0,1]],about_point=q.o)
            for line in target:
                a,b=line.get_start(),line.get_end()
                if abs(a[0]-b[0])<.01:
                    if a[0]<.45 or a[0]>6.5:line.set_opacity(0)
                else:
                    a[0]=.45;b[0]=6.5;line.put_start_and_end_on(a,b)
            self.play(Transform(q.lines,target),right.animate.apply_matrix([[2,0],[0,1]],about_point=q.o),*[dot.animate.move_to(q.p(2*x,y)) for dot,(x,y) in zip(dots,[(-1,1),(1,1),(.5,-.5)])],run_time=3.5)
            self.reveal(self.annotation('საწყისი',[-3.6,2.5],26),self.annotation('გარდაქმნილი',[3.5,2.5],26,YELLOW),self.equation(mathrow('(x₁, x₂)','→',('(2x₁, x₂)',YELLOW),size=42),(0,-3.2)))
        else:
            p=self.plane(origin=(-1.8,-.8),unit=1.05);self.add(p.lines.copy().set_opacity(.22))
            area=p.poly([(0,0),(1,0),(1,2),(0,2)],YELLOW,.18);a=p.arrow((1,2));self.reveal(area);self.play(GrowArrow(a),run_time=1.7)
            m=matrix([[2,0],[0,1]],colors=[GREEN,RED],size=45).move_to([4.1,1.3,0]);self.reveal(backed(m,.25))
            self.play(VGroup(p.lines,area,a).animate.apply_matrix([[2,0],[0,1]],about_point=p.o),run_time=3.2)
            self.reveal(self.endpoint(p,(2,2),'(2, 2)',YELLOW,RIGHT),self.annotation('(1, 2) → (2, 2)',[3.4,-2.8],43,YELLOW,width=6.3))
    def draw_matrix(self):self.stretch_scene()
    def draw_stretch(self):self.stretch_scene(True)
    def draw_columns(self):
        p=self.plane(origin=(-3.5,-1.6),unit=1.15);i,j=self.basis(p);self.beat();self.add(p.lines.copy().set_opacity(.25))
        self.play(p.lines.animate.apply_matrix([[1,1],[0,1]],about_point=p.o),Transform(j,p.arrow((1,1),RED)),FadeOut(self.basis_labels),run_time=3)
        m=matrix([[1,1],[0,1]],colors=[GREEN,RED],size=46,dx=1.1).move_to([3.3,1.4,0])
        self.add(BackgroundRectangle(m,color=BG,fill_opacity=.97,buff=.2).set_z_index(2))
        m.set_z_index(4)
        self.play(TransformFromCopy(i,VGroup(m.cells[0],m.cells[2])),TransformFromCopy(j,VGroup(m.cells[1],m.cells[3])),Create(m[1]),run_time=2);self.reveal(self.annotation('A =',[1.3,1.4],42))
        self.play(Transform(i,p.arrow((2,0),GREEN)),run_time=1.6);self.play(Transform(j,p.arrow((3,1),RED,start=(2,0))),run_time=2)
        self.play(GrowArrow(p.arrow((3,1))),run_time=1.5)
        self.reveal(self.annotation('2(1, 0) + (1, 1)',[3.2,-1.2],39,width=6),self.annotation('= (3, 1)',[3.2,-2.2],47,YELLOW))
    def draw_matrix_question(self):
        p=self.plane(origin=(-4,-1.4),unit=1.1);self.basis(p)
        eq=mathrow(matrix([[1,1],[0,1]],colors=[GREEN,RED],size=51),matrix([[1],[2]],row_colors=[GREEN,RED],size=51),'= ?',size=55,gap=.35)
        self.reveal(self.equation(eq,(2.5,.8)),self.annotation('ერთი პირველი + ორი მეორე სვეტი',[2.3,-1.8],25,width=7.4))
    def draw_matrix_answer(self):
        p=self.plane(origin=(-3.8,-1.8),unit=1.2);a=p.arrow((1,0),GREEN);b=p.arrow((2,2),RED)
        self.play(GrowArrow(a),GrowArrow(b),run_time=2);self.add(b.copy().set_opacity(.2))
        self.play(Transform(b,p.arrow((3,2),RED,start=(1,0))),run_time=2.6);self.play(GrowArrow(p.arrow((3,2))),run_time=1.8)
        eq=mathrow(matrix([[1],[0]],colors=[GREEN]),'+','2',matrix([[1],[1]],colors=[RED]),size=40,gap=.15)
        self.reveal(self.equation(eq,(3.5,1.5)),self.annotation('= (3, 2)',[3.5,-.3],52,YELLOW))
    def draw_composition(self):
        ps=[self.plane(origin=(x,-.7),unit=1.25,bounds=(x-2.6,x+2.6,-2.7,2.1),numbers=False) for x in [-3.4,3.4]];arrows=[]
        for p in ps:
            a=p.arrow((1,0),BLUE);arrows.append(a);self.add(a.copy().set_opacity(.3));self.play(GrowArrow(a),run_time=.7)
        self.reveal(self.annotation('გაჭიმვა → ბრუნვა',[-3.4,2.5],26),self.annotation('ბრუნვა → გაჭიმვა',[3.4,2.5],26))
        self.play(Transform(arrows[0],ps[0].arrow((2,0),GREEN)),Rotate(arrows[1],PI/2,about_point=ps[1].o),run_time=2);self.beat()
        self.play(Rotate(arrows[0],PI/2,about_point=ps[0].o),arrows[1].animate.set_color(RED),run_time=2)
        self.reveal(self.endpoint(ps[0],(0,2),'(0, 2)',GREEN,RIGHT),self.endpoint(ps[1],(0,1),'(0, 1)',RED,RIGHT),self.equation(mathrow(('B(Ax)',GREEN),'≠',('A(Bx)',RED),size=49),(0,-3.1)))
    def draw_dot(self):
        left=matrix([[2],[-1]],row_colors=[GREEN,RED],size=65,dy=1.05).move_to([-3.3,.9,0]);right=matrix([[3],[1]],row_colors=[GREEN,RED],size=65,dy=1.05).move_to([-.9,.9,0])
        self.reveal(left,at('·',[-2.1,.9],60),right,at('w',[-3.3,2.5],34,BLUE),at('x',[-.9,2.5],34,BLUE))
        terms=VGroup(at('2 × 3',[2.6,1.45],53,GREEN),at('(−1) × 1',[2.6,.25],53,RED))
        self.play(TransformFromCopy(VGroup(left.cells[0],right.cells[0]),terms[0]),run_time=1.8)
        self.play(TransformFromCopy(VGroup(left.cells[1],right.cells[1]),terms[1]),run_time=1.8);self.beat()
        eq=mathrow(('6',GREEN),'+',('(−1)',RED),'=',('5',YELLOW),size=67).move_to([0,-2.1,0])
        self.play(TransformFromCopy(terms,eq),run_time=2.2);self.reveal(at('ერთი რიცხვი',[0,-3.05],24,MUTED))
    def draw_projection(self):
        p=self.plane(origin=(-.3,-.5),unit=1.25);self.play(GrowArrow(p.arrow((1,0),GREEN)),run_time=1)
        a=p.arrow((2,1));self.play(GrowArrow(a),run_time=1.5)
        shadow=Line(p.p(0,0),p.p(2,0),color=BLUE,stroke_width=8).set_z_index(4);drop=DashedLine(p.p(2,1),p.p(2,0),color=INK,stroke_opacity=.8)
        score=self.annotation('w · x = 2',[-4.6,1.9],47,BLUE);self.reveal(shadow,drop,score,self.annotation('w = (1, 0)',[-4.6,.9],32,GREEN));self.beat()
        self.play(Transform(a,p.arrow((0,2))),FadeOut(shadow),FadeOut(drop),Transform(score,self.annotation('w · x = 0',[-4.6,1.9],47,BLUE)),run_time=2.6);self.beat()
        self.play(Transform(a,p.arrow((-2,1))),Transform(score,self.annotation('w · x = −2',[-4.6,1.9],43,RED)),Create(Line(p.p(0,0),p.p(-2,0),color=RED,stroke_width=8)),Create(DashedLine(p.p(-2,1),p.p(-2,0),color=INK)),run_time=2.6)
        self.reveal(self.annotation('მიმართულებიანი პროექცია',[2.4,-2.8],28,width=7))
    def classplane(self):
        p=self.plane(origin=(-3.3,-2.5),unit=1.05);self.add(self.annotation('სიგანე',[3,-2.8],22,MUTED),self.annotation('სიმაღლე',[-4.3,2.6],22,MUTED));return p
    def marker(self,p,xy,apple=True,outline=False):
        c=GREEN if apple else RED
        if outline:return Circle(.13,color=c,stroke_width=3).move_to(p.p(*xy)).set_z_index(8)
        return (Dot(p.p(*xy),radius=.105,color=c) if apple else Triangle(color=c,fill_opacity=1,stroke_width=1).scale(.13).move_to(p.p(*xy))).set_z_index(8)
    def data_points(self,p):
        data=[(3,1,True),(4,2,True),(4,3,True),(1,3,False),(2,4,False),(1,4,False)]
        return VGroup(*[self.marker(p,(x,y),a) for x,y,a in data]),data
    def boundary(self,p,b=0,color=YELLOW):
        low=max(0,-b);high=min(5,5-b);return Line(p.p(low,low+b),p.p(high,high+b),color=color,stroke_width=3.5).set_z_index(3)
    def regions(self,p):return VGroup(p.poly([(0,0),(5,0),(5,5)],GREEN,.045).set_stroke(opacity=0),p.poly([(0,0),(0,5),(5,5)],RED,.045).set_stroke(opacity=0))
    def draw_classifier(self):
        p=self.classplane();pts,_=self.data_points(p);self.add(self.regions(p));self.play(LaggedStart(*[GrowFromCenter(x) for x in pts],lag_ratio=.15),run_time=2)
        self.play(Create(self.boundary(p)),run_time=2.5)
        self.reveal(self.annotation('s = x₁ − x₂',[4.1,1.8],41,YELLOW,width=4.5),self.annotation('s ≥ 0',[4.1,.5],36,GREEN),self.annotation('ვაშლი',[4.1,-.1],27,GREEN),self.annotation('s < 0',[-5.1,.1],36,RED),self.annotation('მსხალი',[-5.1,-.5],27,RED))
    def draw_boundary(self):
        p=self.classplane();self.add(self.regions(p),self.boundary(p));d=self.marker(p,(3,2),True,True).scale(1.4);score=self.annotation('s = +1',[4.4,1.2],53,GREEN)
        self.reveal(d,score,self.annotation('x₂ = x₁',[-4.9,1.4],37,YELLOW));self.beat()
        self.play(d.animate.move_to(p.p(2.5,2.5)),Transform(score,self.annotation('s = 0',[4.4,1.2],53,YELLOW)),run_time=2);self.beat()
        self.play(d.animate.move_to(p.p(2,3)).set_color(RED),Transform(score,self.annotation('s = −1',[4.4,1.2],53,RED)),run_time=2);self.reveal(self.annotation('პასუხი შეიცვალა',[4.4,-.1],26,RED,width=4.3))
    def draw_bias(self):
        p=self.classplane();line=self.boundary(p);self.add(line,line.copy().set_opacity(.2));point=self.marker(p,(2,2.5),False,True).scale(1.4);self.reveal(point)
        value=self.annotation('b = 0',[4.3,1.8],55,BLUE);eq=self.annotation('x₂ = x₁',[4.3,.55],35,YELLOW);self.reveal(value,eq);self.beat()
        self.play(Transform(line,self.boundary(p,1)),Transform(value,self.annotation('b = 1',[4.3,1.8],55,BLUE)),Transform(eq,self.annotation('x₂ = x₁ + 1',[4.3,.55],34,YELLOW,width=4.5)),point.animate.set_color(GREEN),run_time=3)
        self.reveal(self.annotation('s = x₁ − x₂ + b',[3.4,-2.8],37,width=6))
    def draw_scores(self):
        w=matrix([[1,-1],[-1,1]],row_colors=[GREEN,RED],size=53,dx=1.05,dy=1.2).move_to([-4.4,.3,0]);x=matrix([[4],[1]],colors=[BLUE],size=53,dy=1.2).move_to([-1.5,.3,0])
        self.reveal(w,x,at('W',[-4.4,2.2],33),at('x',[-1.5,2.2],33,BLUE))
        for i,(c,v,y) in enumerate([(GREEN,3,1),(RED,-3,-.8)]):
            box=SurroundingRectangle(VGroup(*w.cells[i*2:i*2+2]),color=c,buff=.13);self.play(Create(box),run_time=.6)
            bar=Rectangle(width=abs(v)*.72,height=.42,stroke_width=0,fill_color=c,fill_opacity=.8).move_to([2.5+(1 if v>0 else -1)*abs(v)*.36,y,0])
            self.reveal(Line([2.5,y-.6,0],[2.5,y+.6,0],color=MUTED));self.play(GrowFromPoint(bar,[2.5,y,0]),run_time=1.6)
            self.reveal(at(str(v).replace('-','−'),[5.6,y],51,c));self.play(FadeOut(box),run_time=.4)
        self.reveal(self.equation(mathrow('Wx =',matrix([[3],[-3]],row_colors=[GREEN,RED],size=41,dy=.65),size=40),(0,-2.8)))
    def draw_batch(self):
        x=matrix([[3,1],[1,3],[2,2]],colors=[GREEN,RED],size=46,dx=.9,dy=.95).move_to([-4.7,.3,0]);w=matrix([[1,-1],[-1,1]],size=46,dx=.9,dy=.95).move_to([-.4,.3,0]);out=matrix([['?','?'],['?','?'],['?','?']],size=46,dx=.9,dy=.95).move_to([4.3,.3,0])
        self.reveal(x,w,out,at('×',[-2.5,.3],45),at('=',[1.9,.3],45),at('X',[-4.7,2.5],35,BLUE),at('Wᵀ',[-.4,2.5],35,YELLOW),at('ქულები',[4.3,2.5],28))
        row=SurroundingRectangle(VGroup(x.cells[0],x.cells[1]),color=YELLOW,buff=.12);col=SurroundingRectangle(VGroup(w.cells[0],w.cells[2]),color=YELLOW,buff=.12)
        self.play(Create(row),Create(col),run_time=1)
        self.reveal(mathrow(('3',GREEN),'× 1 +',('1',RED),'× (−1) =',('2',YELLOW),size=41).move_to([0,-2.6,0]));self.beat()
        self.play(Transform(out,matrix([[2,-2],[-2,2],[0,0]],size=46,dx=.9,dy=.95).move_to(out)),FadeOut(row),FadeOut(col),run_time=2)
    def draw_training(self):
        p=self.classplane();pts,data=self.data_points(p);self.add(pts);line=self.boundary(p,-2,RED);self.add(line)
        count=lambda b:sum((x-y+b>=0)!=target for x,y,target in data)
        lab=self.annotation('b = −2',[4.3,1.8],48,BLUE);score=self.annotation(f'{count(-2)} / 6',[4.3,.35],62,RED);mistake=Circle(.22,color=RED,stroke_width=3).move_to(p.p(4,3))
        self.reveal(lab,score,mistake,self.annotation('შეცდომა',[4.3,-.5],25,MUTED));self.beat()
        for b in [-1,0]:
            self.play(Transform(line,self.boundary(p,b)),Transform(lab,self.annotation(f'b = {str(b).replace("-","−")}',[4.3,1.8],48,BLUE)),Transform(score,self.annotation(f'{count(b)} / 6',[4.3,.35],62,GREEN)),mistake.animate.set_opacity(0),run_time=2.5);self.beat()
        self.reveal(self.annotation('ვცვლით → ვამოწმებთ',[3.8,-2.6],27,width=5.5))
    def draw_loss(self):
        for x,pred,target,c in [(-3.6,2,3,GREEN),(2.1,5,3,RED)]:
            o=np.array([x,-2.2,0]);u=.65;targetdot=Dot(o+UP*target*u,color=INK,radius=.075);preddot=Dot(o+UP*pred*u,color=BLUE,radius=.09)
            residual=Line(preddot.get_center(),targetdot.get_center(),color=c,stroke_width=7)
            self.reveal(Line(o,o+UP*3.6,color=MUTED),targetdot,preddot,at(str(pred),preddot.get_center()+LEFT*.4,32,BLUE),at('3',targetdot.get_center()+LEFT*.4,32))
            self.play(Create(residual),run_time=1.2)
            square=Square(side_length=abs(pred-target)*u,color=c,fill_opacity=.25,stroke_width=2).next_to(residual,RIGHT,buff=.2).align_to(residual,DOWN)
            self.play(TransformFromCopy(residual,square),run_time=1.8);self.reveal(at(str((pred-target)**2),square.get_center(),38,c))
        self.reveal(self.equation(mathrow('L = (',('1',GREEN),'+',('4',RED),') / 2 =',('2.5',YELLOW),size=42),(0,-3.05)),self.annotation('შეცდომა²',[-.4,2.3],35,YELLOW))
    def draw_generalization(self):
        p=self.classplane();pts,_=self.data_points(p);self.add(pts,self.boundary(p));self.reveal(self.annotation('ნანახი მაგალითები',[4.1,2],27,width=5.2))
        for xy,apple in [((3.5,1.5),True),((1.5,3.5),False),((2,3),True),((3,2),False)]:self.play(GrowFromCenter(self.marker(p,xy,apple,True).scale(1.2)),run_time=.7)
        self.reveal(self.annotation('ახალი მაგალითები',[4.1,1],27,BLUE,width=5.2))
        for xy in [(2,3),(3,2)]:self.play(Create(Cross(stroke_color=YELLOW,stroke_width=3).scale(.15).move_to(p.p(*xy)+RIGHT*.33)),run_time=.6)
        self.reveal(self.annotation('ნანახზე კარგი ≠ ყველგან კარგი',[2.8,-2.95],28,YELLOW,width=7.7))
    def network(self,sizes,spacing=2.1):
        nodes=[];edges=[]
        for i,n in enumerate(sizes):nodes.append(VGroup(*[Circle(radius=.13,color=INK,stroke_width=1.5,fill_color=BLUE,fill_opacity=.15+((i+j)%4)*.18).move_to([(i-(len(sizes)-1)/2)*spacing,(j-(n-1)/2)*.48+(i%2)*.12,0]) for j in range(n)]))
        for a,b in zip(nodes[:-1],nodes[1:]):edges.append(VGroup(*[Line(x.get_center(),y.get_center(),color=BLUE if (i+j)%3 else RED,stroke_width=.7,stroke_opacity=.45) for i,x in enumerate(a) for j,y in enumerate(b)]))
        return VGroup(*edges,*nodes),nodes,edges
    def draw_network(self):
        net,nodes,edges=self.network([6,8,6,3],2.9);net.scale(1.15);self.play(Create(net),run_time=2.4)
        for e in edges:self.pulse(e)
        self.beat();self.play(FadeOut(net),run_time=.8)
        ins=[np.array([-4.6,1,0]),np.array([-4.6,-1.3,0])];outs=[np.array([2.4,1.85,0]),np.array([2.4,-.05,0]),np.array([2.4,-1.95,0])];weighted=[(0,0,1),(1,1,1),(0,2,1),(1,2,-1)]
        connections=VGroup(*[Line(ins[i],outs[j],color=GREEN if w>0 else RED,stroke_width=2,stroke_opacity=.6) for i,j,w in weighted]);self.reveal(connections)
        circles=VGroup(*[Circle(.44,color=BLUE,fill_color=BG,fill_opacity=1).move_to(q) for q in ins],*[Circle(.48,color=YELLOW,fill_color=BG,fill_opacity=1).move_to(q) for q in outs]);self.reveal(circles,*[at(str(v),q,40,BLUE).set_z_index(10) for q,v in zip(ins,[2,1])])
        for j,v in enumerate([2,1,1]):self.pulse([connections[k] for k,t in enumerate(weighted) if t[1]==j]);self.reveal(at(str(v),outs[j],40,YELLOW).set_z_index(10))
        self.reveal(backed(matrix([[1,0],[0,1],[1,-1]],size=29,dx=.7,dy=.55).move_to([-1.2,.1,0]),.25),self.annotation('z = Wx',[5.1,.05],37,YELLOW,width=3),self.annotation('b = 0',[-1.3,-2.9],29,MUTED))
    def draw_relu(self):
        p=self.plane(origin=(-.8,-.7),unit=1.08);graph=VMobject(color=YELLOW,stroke_width=5).set_points_as_corners([p.p(-5,0),p.p(0,0),p.p(3.2,3.2)])
        self.play(Create(graph),run_time=2.5);self.reveal(self.annotation('ReLU(z) = max(0, z)',[-3.8,2],39,YELLOW,width=6))
        points=VGroup(*[self.dot(p,(x,x),BLUE,.09) for x in [-2,1,3]]);self.reveal(points);self.beat()
        self.play(points[0].animate.move_to(p.p(-2,0)).set_color(RED),points[1].animate.set_color(GREEN),points[2].animate.set_color(GREEN),run_time=2.2)
        self.reveal(self.annotation('(−2, 1, 3) → (0, 1, 3)',[2.1,-2.9],38,width=8.8),self.annotation('z',[6,-.95],28),self.annotation('ReLU(z)',[.2,2.45],23,MUTED))
    def draw_quiz(self):
        p=self.plane(origin=(-3.8,-1.8),unit=1.1);self.play(GrowArrow(p.arrow((2,3),BLUE)),run_time=2);self.reveal(self.endpoint(p,(2,3),'x = (2, 3)',BLUE,UP))
        self.reveal(self.annotation('w = (1, −1)',[3.7,1.7],43),self.annotation('b = 2',[3.7,.7],43,YELLOW),self.annotation('1. s = ?',[3.7,-.5],35),self.annotation('2. რომელი კატეგორია?',[3.7,-1.35],27,width=5.7),self.annotation('3. თუ x = (2, 5)?',[3.7,-2.2],29,width=5.7),self.annotation('s ≥ 0: ვაშლი · s < 0: მსხალი',[-2.8,-3.1],22,MUTED,width=7))
    def draw_quiz_answer(self):
        p=self.classplane();self.play(Create(self.boundary(p,2)),run_time=2);a=self.marker(p,(2,3),True);b=self.marker(p,(2,5),False)
        self.reveal(a,self.annotation('2 − 3 + 2 = 1',[4.1,1.7],38,GREEN,width=4.8));self.beat();self.play(TransformFromCopy(a,b),run_time=1.8)
        self.reveal(self.annotation('2 − 5 + 2 = −1',[4.1,.6],36,RED,width=4.8),self.annotation('x₂ = x₁ + 2',[4.1,-1],36,YELLOW,width=4.8),self.annotation('ვაშლი → მსხალი',[3.5,-2.7],31,width=6))
    def draw_recap(self):
        xs=[-5.1,-1.7,1.7,5.1]
        for x in xs:self.add(Line([x-1.3,-.8,0],[x+1.3,-.8,0],color=GRID),Line([x,-1.8,0],[x,1.4,0],color=GRID))
        arrow=Arrow([xs[0]-.8,-.8,0],[xs[0]+.7,1.1,0],color=BLUE,buff=0)
        poly=Polygon([xs[1]-.9,-.8,0],[xs[1]+.4,-.8,0],[xs[1]+1,1,0],[xs[1]-.3,1,0],color=YELLOW,fill_opacity=.2)
        score=txt('w · x',43,GREEN).move_to([xs[2],.2,0]);points=VGroup(*[Dot([xs[3]+dx,y,0],radius=.09,color=c) for dx,y,c in [(-.6,-.4,GREEN),(.5,-.2,GREEN),(-.5,1,RED),(.5,.8,RED)]],Line([xs[3]-1,.35,0],[xs[3]+1,.35,0],color=YELLOW))
        for obj in [arrow,poly,score,points]:self.reveal(obj)
        for x,name,c in zip(xs,['ვექტორი','მატრიცა','ქულა','პროგნოზი'],[BLUE,YELLOW,GREEN,INK]):self.reveal(at(name,[x,-2.25],28,c))
        self.reveal(at('კითხვები',[0,2.4],34))

for _n in range(1,31):globals()[f'S{_n:02}']=type(f'S{_n:02}',(Talk,),{'number':_n,'__module__':__name__})
