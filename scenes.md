# Complete scene storyboard

Georgian live lesson; 30 scenes; 45:00 including discussion. Audience: high-school beginners with algebra and coordinate-graph knowledge; no previous vectors, matrices or ML.

Narrative: measurable objects → vectors → combinations → transformations → scores → decisions → learning → networks. Three retrieval exercises precede their answer scenes.

## Design and notation

See design-notes.md. Green = first component/basis or positive contribution; rose = second component/basis or negative contribution; cyan = input/data; yellow = result or boundary. Direct labels and category shapes provide redundant cues. The geometry is generated from coordinates, never approximated by artwork. Arrows/axes use a common unit on each plane.

## 01. წრფივი ალგებრა მანქანური სწავლებისთვის

- Duration: 00:00–01:00 (60 seconds).
- Objective: გავაჩინოთ ინტერესი და გავაცნოთ გაკვეთილის მიზანი.
- Central insight: წრფივი ალგებრა მანქანური სწავლებისთვის
- Mathematical content: რიცხვები → ვექტორები → მოდელი
- Composition, diagram and animation: Large title beside a full-height changing basis and translucent parallelogram.
- Exact construction: `visual_scenes.py`, `draw_cover()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/01.jpg`.

### Speaker notes

დღეს ვნახავთ, როგორ შეიძლება კომპიუტერმა რიცხვებით აღწეროს საგანი და ამ რიცხვების მიხედვით მიიღოს გადაწყვეტილება. დაგვჭირდება მხოლოდ შეკრება, გამრავლება და კოორდინატები.

ბოლოს თავად გამოთვლით პატარა მოდელის პასუხს. ყველა მაგალითი სასწავლოა: აქ გამოყენებული ხილის მონაცემები და წესები გამოგონილია.

გააცანით ფორმატი: ჯერ ვუყურებთ მოძრაობას, შემდეგ ვჩერდებით, ვმსჯელობთ და ვცდილობთ პასუხის წინასწარ გამოცნობას.

**Transition:** Use this result to introduce “წესს მაგალითებიდან ვპოულობთ”. The next scene begins from its opening state, with no preview of its result.

## 02. წესს მაგალითებიდან ვპოულობთ

- Duration: 01:00–02:30 (90 seconds).
- Objective: განვასხვაოთ სწავლა და უკვე ნასწავლი მოდელის გამოყენება.
- Central insight: წესს მაგალითებიდან ვპოულობთ
- Mathematical content: მაგალითები → სწავლა → ახალი პასუხი
- Composition, diagram and animation: Labeled examples form two clusters; a boundary and an unseen point establish the prediction question.
- Exact construction: `visual_scenes.py`, `draw_ml()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/02.jpg`.

### Speaker notes

წარმოიდგინეთ, რომ გვინდა ვაშლისა და მსხლის გარჩევა. პროგრამას შეგვიძლია მზა წესი მივცეთ; მანქანური სწავლებისას კი წესის რიცხვით პარამეტრებს მაგალითების დახმარებით ვარჩევთ.

სასწავლო მაგალითში გვაქვს აღწერა და სწორი პასუხი. სწავლა ამ მაგალითებზე შეცდომის შემცირებას ცდილობს. გამოყენებისას მოდელს ვაძლევთ ახალ აღწერას და ვიღებთ პროგნოზს.

კომპიუტერს არ აქვს ადამიანის მსგავსი გაგება. პასუხი შეიძლება მცდარი იყოს. ჰკითხეთ აუდიტორიას, რომელი ნიშნით არჩევენ თვითონ ამ ორ ხილს.

**Transition:** Use this result to introduce “რიცხვები აღწერს საგანს”. The next scene begins from its opening state, with no preview of its result.

## 03. რიცხვები აღწერს საგანს

- Duration: 02:30–04:00 (90 seconds).
- Objective: შემოვიტანოთ ნიშანი და ნიშნების ფიქსირებული მიმდევრობა.
- Central insight: რიცხვები აღწერს საგანს
- Mathematical content: x = [2, 3]
- Composition, diagram and animation: Large fruit silhouette, width/height measurement lines, then a color-linked column vector.
- Exact construction: `visual_scenes.py`, `draw_features()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/03.jpg`.

### Speaker notes

ავირჩიოთ ორი ნიშანი: სიგანე და სიმაღლე, ორივე ერთსა და იმავე პირობით ერთეულში. ჩვენი პირველი საგნის სიგანეა 2, სიმაღლე — 3. ეს რეალური გაზომვები არ არის.

ყოველთვის ჯერ სიგანეს ჩავწერთ, შემდეგ სიმაღლეს. [2, 3] და [3, 2] სხვადასხვა აღწერაა. რიცხვებს მნიშვნელობას აძლევს ის, თუ რა გავზომეთ და რა რიგით ჩავწერეთ.

ორი ნიშანი ავირჩიეთ, რათა ნახატი სიბრტყეზე მოთავსდეს. რეალურ ამოცანაში შეიძლება ასობით ან ათასობით ნიშანი გვქონდეს.

**Transition:** Use this result to introduce “ვექტორი აერთიანებს კოორდინატებს”. The next scene begins from its opening state, with no preview of its result.

## 04. ვექტორი აერთიანებს კოორდინატებს

- Duration: 04:00–05:30 (90 seconds).
- Objective: დავაკავშიროთ რიცხვების სია, წერტილი და ისარი.
- Central insight: ვექტორი აერთიანებს კოორდინატებს
- Mathematical content: x = (2, 3)
- Composition, diagram and animation: Full-frame plane; horizontal and vertical components lead to a large vector; coordinate matrix remains beside its endpoint.
- Exact construction: `visual_scenes.py`, `draw_vector()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/04.jpg`.

### Speaker notes

ვექტორს აქ რიცხვების დალაგებული სიის სახით ვიყენებთ. ორი რიცხვი გვაძლევს სიბრტყეზე წერტილის კოორდინატებს. საწყისიდან ამ წერტილამდე დახატული ისარი იმავე ვექტორს აჩვენებს.

გაჰყევით მოძრაობას: ორი ნაბიჯი მარჯვნივ, სამი ზემოთ. მეორე კოორდინატი არ ნიშნავს მეორე ცალკე წერტილს. ორივე ერთად აღწერს ერთ საგანს.

აღნიშნეთ, რომ მონაცემის ვექტორი ფიზიკურ მოძრაობას არ მოითხოვს. ისარი გვეხმარება რიცხვების ურთიერთობის დანახვაში. სთხოვეთ მოსწავლეს ახსნას, სად იქნებოდა (3,2).

**Transition:** Use this result to introduce “შეკრება აერთიანებს გადაადგილებებს”. The next scene begins from its opening state, with no preview of its result.

## 05. შეკრება აერთიანებს გადაადგილებებს

- Duration: 05:30–07:00 (90 seconds).
- Objective: შეკრება დავინახოთ როგორც გადაადგილებების მიმდევრობა.
- Central insight: შეკრება აერთიანებს გადაადგილებებს
- Mathematical content: (2, 1) + (1, 2) = (3, 3)
- Composition, diagram and animation: Full-frame tip-to-tail addition, ghost arrows, and a highlighted resultant.
- Exact construction: `visual_scenes.py`, `draw_addition()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/05.jpg`.

### Speaker notes

ჯერ ავიღოთ (2,1), შემდეგ (1,2). მეორე ისარი შეგვიძლია გადავიტანოთ პირველის ბოლოში: მისი სიგრძე და მიმართულება უცვლელია.

საბოლოო წერტილი არის (3,3). კოორდინატებით ვკრებთ შესაბამის რიცხვებს: 2+1 და 1+2. ისრების ნახატი და რიცხვების მოქმედება ერთსა და იმავეს გვიყვება.

ხილის ორი აღწერის ჯამი ახალ რეალურ ხილს ავტომატურად არ ნიშნავს. ეს მათემატიკური მოქმედებაა; მისი პრაქტიკული მნიშვნელობა ამოცანაზეა დამოკიდებული. ჰკითხეთ, შეიცვლება თუ არა ჯამი რიგის შეცვლით.

**Transition:** Use this result to introduce “რიცხვი ცვლის ვექტორის მასშტაბს”. The next scene begins from its opening state, with no preview of its result.

## 06. რიცხვი ცვლის ვექტორის მასშტაბს

- Duration: 07:00–08:30 (90 seconds).
- Objective: დავინახოთ სიგრძისა და მიმართულების ცვლილება.
- Central insight: რიცხვი ცვლის ვექტორის მასშტაბს
- Mathematical content: 2(1, 1) = (2, 2)     −1(1, 1) = (−1, −1)
- Composition, diagram and animation: Full-frame scalar multiplication; the multiplier and vector change together while previous states leave a faint reference.
- Exact construction: `visual_scenes.py`, `draw_scaling()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/06.jpg`.

### Speaker notes

როდესაც ვექტორს 2-ზე ვამრავლებთ, ორივე კოორდინატს ვაორმაგებთ. ისარი იმავე მიმართულებით რჩება და ორჯერ გრძელდება.

ნახევარზე გამრავლება ამოკლებს, უარყოფით რიცხვზე გამრავლება მიმართულებასაც აბრუნებს. ნულზე გამრავლებით მივიღებთ ნულოვან ვექტორს.

უარყოფითი სიგანე ხილის გაზომვას ვერ აღწერს, მაგრამ უარყოფითი კოორდინატები ზოგად ვექტორულ სივრცეში სრულიად დასაშვებია. მაგალითად, მათ შეუძლიათ საშუალოდან გადახრა აღწერონ.

**Transition:** Use this result to introduce “სად მიგვიყვანს ორი მიმართულება?”. The next scene begins from its opening state, with no preview of its result.

## 07. სად მიგვიყვანს ორი მიმართულება?

- Duration: 08:30–10:30 (120 seconds).
- Objective: მოსწავლეებმა თავად ააგონ წრფივი კომბინაცია.
- Central insight: სად მიგვიყვანს ორი მიმართულება?
- Mathematical content: 2(1, 0) + 3(0, 1) = ?
- Composition, diagram and animation: Full-frame basis exercise with a large unanswered linear combination.
- Exact construction: `visual_scenes.py`, `draw_exercise()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/07.jpg`.

### Speaker notes

20 წამი დაუთმეთ პირობის წაკითხვას. პირველი ისარი ერთი ნაბიჯია მარჯვნივ, მეორე — ერთი ნაბიჯი ზემოთ. პირველი ორჯერ გვჭირდება, მეორე — სამჯერ.

მიეცით 40 წამი ინდივიდუალური ფიქრისთვის და 30 წამი მეზობელთან შედარებისთვის. სთხოვეთ პასუხი როგორც წყვილით, ისე პატარა ნახატით.

ბოლო 30 წამში მოისმინეთ ორი განსხვავებული ახსნა. პასუხი ჯერ არ გაამხილოთ. გავრცელებული შეცდომაა მხოლოდ რიცხვების შეკრება და პასუხად 5-ის დაწერა.

**Audience task:** რა ვექტორს მივიღებთ?

**Expected answer:** (2, 3)

**Transition:** Use this result to introduce “საბაზისო ვექტორები”. The next scene begins from its opening state, with no preview of its result.

## 08. საბაზისო ვექტორები

- Duration: 10:30–11:30 (60 seconds).
- Objective: ავხსნათ საბაზისო მიმართულებების იდეა.
- Central insight: საბაზისო ვექტორები
- Mathematical content: (2, 3) = 2e₁ + 3e₂
- Composition, diagram and animation: Repeated basis steps resolve to one vector and a color-linked matrix equation.
- Exact construction: `visual_scenes.py`, `draw_basis()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/08.jpg`.

### Speaker notes

პასუხია (2,3). პირველი მიმართულება გვაძლევს ჰორიზონტალურ ნაწილს, მეორე — ვერტიკალურს. ამ ორი ისრის რიცხვებზე გამრავლებითა და შეკრებით სიბრტყის ნებისმიერ წერტილამდე მივალთ.

მათ სტანდარტული ბაზისის ვექტორები ეწოდება: e₁=(1,0), e₂=(0,1). სახელის დაზეპირება აუცილებელი არ არის; მთავარი ისაა, რომ ორი დამოუკიდებელი მიმართულებით ყველა ვექტორი ავაწყოთ.

ეს ხიდია მატრიცისკენ: თუ ვიცით, სად მიდის თითოეული საბაზისო ისარი, მალე ნებისმიერი ვექტორის ახალ მდებარეობასაც ვიპოვით.

**Transition:** Use this result to introduce “ერთი მიმართულება მხოლოდ წრფეს ფარავს”. The next scene begins from its opening state, with no preview of its result.

## 09. ერთი მიმართულება მხოლოდ წრფეს ფარავს

- Duration: 11:30–13:00 (90 seconds).
- Objective: ვაჩვენოთ, რატომ გვჭირდება დამოუკიდებელი მიმართულებები.
- Central insight: ერთი მიმართულება მხოლოდ წრფეს ფარავს
- Mathematical content: a(1, 1) → ერთი წრფე
- Composition, diagram and animation: Several multiples lie on one bright line; an unreachable point sits visibly off it.
- Exact construction: `visual_scenes.py`, `draw_span()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/09.jpg`.

### Speaker notes

თუ მხოლოდ (1,1) გვაქვს, მისი გამრავლებით ყველა წერტილს ვერ მივწვდებით. რამდენჯერაც უნდა გავზარდოთ ან შევაბრუნოთ, ყოველთვის იმავე დიაგონალზე ვრჩებით.

მეორე ისარი (2,2) არაფერს ცვლის: ის უკვე პირველის ორმაგია. დამოუკიდებელი ახალი მიმართულება გვჭირდება, მაგალითად (1,0).

ჰკითხეთ, მივაღწევთ თუ არა (2,1)-ს მხოლოდ (1,1)-ის გამრავლებით. აქ არ გვჭირდება ფორმალური თეორემა: ნახატზე ჩანს, რომ პირველი ორი კოორდინატი ყოველთვის ტოლი იქნება.

**Transition:** Use this result to introduce “მატრიცა გარდაქმნის ვექტორს”. The next scene begins from its opening state, with no preview of its result.

## 10. მატრიცა გარდაქმნის ვექტორს

- Duration: 13:00–14:30 (90 seconds).
- Objective: შემოვიტანოთ მატრიცა როგორც გარდაქმნის წესი.
- Central insight: მატრიცა გარდაქმნის ვექტორს
- Mathematical content: A = [[2, 0], [0, 1]]
- Composition, diagram and animation: A large input vector and matrix accompany a live grid stretch.
- Exact construction: `visual_scenes.py`, `draw_matrix()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/10.jpg`.

### Speaker notes

მატრიცა რიცხვების მართკუთხა ცხრილია. ამ მაგალითში ის წესს აღწერს: პირველი კოორდინატი გააორმაგე, მეორე უცვლელი დატოვე.

თუ შეყვანაა (1,2), პასუხია (2,2). ეს არ არის ორივე რიცხვის გაორმაგება. ჰორიზონტალური მიმართულება იჭიმება, ვერტიკალური უცვლელი რჩება.

მატრიცები მონაცემების შესანახადაც გამოიყენება, მაგრამ ახლა ყურადღებას მათ მოქმედებაზე ვამახვილებთ. მომდევნო ნახატზე მთელ ბადეს ერთად გარდავქმნით.

**Transition:** Use this result to introduce “ერთი წესი მოქმედებს მთელ სიბრტყეზე”. The next scene begins from its opening state, with no preview of its result.

## 11. ერთი წესი მოქმედებს მთელ სიბრტყეზე

- Duration: 14:30–16:00 (90 seconds).
- Objective: მატრიცის მოქმედება დავინახოთ ერთდროულად ბევრ წერტილზე.
- Central insight: ერთი წესი მოქმედებს მთელ სიბრტყეზე
- Mathematical content: (x₁, x₂) → (2x₁, x₂)
- Composition, diagram and animation: Equal before/after planes, translucent unit cells, and several tracked points show horizontal stretch.
- Exact construction: `visual_scenes.py`, `draw_stretch()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/11.jpg`.

### Speaker notes

ყოველი წერტილის პირველი კოორდინატი ორმაგდება. ამიტომ ვერტიკალური ბადის ხაზები ერთმანეთს შორდება, ჰორიზონტალური დონეები კი იმავე სიმაღლეზე რჩება.

გააჩერეთ ბოლო კადრი და შეადარეთ რამდენიმე წერტილი. საწყისი (0,0) ისევ საწყისია. სწორი ხაზები სწორ ხაზებად რჩება.

წრფივი გარდაქმნა ინარჩუნებს შეკრებასა და რიცხვზე გამრავლებას: ჯერ შეკრება და შემდეგ გარდაქმნა იმავე შედეგს გვაძლევს, რასაც ცალ-ცალკე გარდაქმნა და შეკრება. მხოლოდ ხაზების სისწორე სრული განსაზღვრება არ არის.

ჰკითხეთ: ყველა ისრის სიგრძე ორმაგდება? ვერტიკალური ისარი გვაძლევს საწინააღმდეგო მაგალითს.

ფორმალური ჩანაწერია T(u+v)=T(u)+T(v) და T(cu)=cT(u), ყველა u,v ვექტორისა და c რიცხვისთვის. ეს ორი პირობა განსაზღვრავს წრფივობას; კერძოდ T(0)=0.

**Transition:** Use this result to introduce “სვეტები გვიჩვენებს ახალ მიმართულებებს”. The next scene begins from its opening state, with no preview of its result.

## 12. სვეტები გვიჩვენებს ახალ მიმართულებებს

- Duration: 16:00–17:30 (90 seconds).
- Objective: ავხსნათ მატრიცა-ვექტორის ნამრავლი სვეტების კომბინაციით.
- Central insight: სვეტები გვიჩვენებს ახალ მიმართულებებს
- Mathematical content: A(2, 1) = 2(1, 0) + 1(1, 1) = (3, 1)
- Composition, diagram and animation: Basis arrows shear with the grid, then their coordinates become matrix columns; a vector is assembled from those columns.
- Exact construction: `visual_scenes.py`, `draw_columns()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/12.jpg`.

### Speaker notes

ახლა სხვა მატრიცა გვაქვს: პირველი სვეტია (1,0), მეორე — (1,1). პირველი გვეუბნება, სად გადავა e₁, მეორე — სად გადავა e₂.

ვექტორი (2,1) ნიშნავს ორ პირველ და ერთ მეორე საბაზისო მიმართულებას. გარდაქმნის შემდეგაც ორი პირველი ახალი ისარი და ერთი მეორე ახალი ისარი უნდა ავიღოთ.

გამოდის 2(1,0)+(1,1)=(3,1). ეს მატრიცა-ვექტორის გამრავლების გეომეტრიული აზრია. თითოეული სვეტი შესატანია, ხოლო შეყვანის კოორდინატები მათ რაოდენობას განსაზღვრავს.

გაიმეორეთ ანიმაცია ერთხელ და ამჯერად მოსწავლეებს სთხოვეთ თქვან, რომელი ისარი სად მიდის.

**Transition:** Use this result to introduce “სად აღმოჩნდება ეს ვექტორი?”. The next scene begins from its opening state, with no preview of its result.

## 13. სად აღმოჩნდება ეს ვექტორი?

- Duration: 17:30–19:00 (90 seconds).
- Objective: დავამაგროთ სვეტების კომბინაციის წესი.
- Central insight: სად აღმოჩნდება ეს ვექტორი?
- Mathematical content: A = [[1, 1], [0, 1]]     x = (1, 2)
- Composition, diagram and animation: Large matrix question with a geometric reference and no answer.
- Exact construction: `visual_scenes.py`, `draw_matrix_question()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/13.jpg`.

### Speaker notes

პირველი 20 წამი დაუთმეთ იმას, თუ რომელი რიცხვებია პირველ და მეორე სვეტში. სთხოვეთ, სვეტი სტრიქონში არ აერიოთ.

შემდეგ 40 წამი მისცეთ გამოსათვლელად: ერთხელ პირველი სვეტი, ორჯერ მეორე. სურვილისამებრ გამოიყენონ ბადე და ისრები.

ბოლო 30 წამი მოისმინეთ ახსნა. სწორი შედეგის გარდა გვაინტერესებს გზა: რატომ გამრავლდა მეორე სვეტი ორზე? პასუხი შემდეგ კადრზეა.

**Audience task:** სად გადავა (1,2)?

**Expected answer:** (3,2)

**Transition:** Use this result to introduce “პასუხს სვეტების კომბინაცია გვაძლევს”. The next scene begins from its opening state, with no preview of its result.

## 14. პასუხს სვეტების კომბინაცია გვაძლევს

- Duration: 19:00–20:00 (60 seconds).
- Objective: შევადაროთ გეომეტრიული და რიცხვითი პასუხები.
- Central insight: პასუხს სვეტების კომბინაცია გვაძლევს
- Mathematical content: (1, 0) + 2(1, 1) = (3, 2)
- Composition, diagram and animation: Full-frame answer construction with color-linked column terms beside the geometry.
- Exact construction: `visual_scenes.py`, `draw_matrix_answer()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/14.jpg`.

### Speaker notes

პირველი სვეტის ერთი ასლი არის (1,0), მეორის ორი ასლი — (2,2). მათი ჯამია (3,2).

სტრიქონებით იგივე პასუხს მივიღებთ: პირველი კომპონენტია 1×1+1×2=3; მეორე — 0×1+1×2=2.

შეადარეთ ორი გზა. სვეტები გვაჩვენებს, როგორ ვაწყობთ გამოსავალ ვექტორს, ხოლო სტრიქონები — როგორ ვითვლით მის თითოეულ კომპონენტს.

**Transition:** Use this result to introduce “მოქმედებების რიგი ცვლის შედეგს”. The next scene begins from its opening state, with no preview of its result.

## 15. მოქმედებების რიგი ცვლის შედეგს

- Duration: 20:00–21:30 (90 seconds).
- Objective: გარდაქმნების მიმდევრობის მნიშვნელობა ვაჩვენოთ.
- Central insight: მოქმედებების რიგი ცვლის შედეგს
- Mathematical content: B(Ax) ≠ A(Bx)  ზოგადად
- Composition, diagram and animation: Two geometric routes show stretch/rotation in different orders, preserving the original vector as a ghost.
- Exact construction: `visual_scenes.py`, `draw_composition()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/15.jpg`.

### Speaker notes

ავიღოთ x=(1,0). A ჰორიზონტალურ კოორდინატს აორმაგებს, B კი 90 გრადუსით საათის ისრის საწინააღმდეგოდ აბრუნებს.

ჯერ A: (1,0) ხდება (2,0); შემდეგ B: მივიღებთ (0,2). პირიქით, ჯერ B გვაძლევს (0,1)-ს, რომელსაც ჰორიზონტალური გაჭიმვა აღარ ცვლის.

ამიტომ B(Ax) და A(Bx) ზოგადად სხვადასხვა პასუხია. BA ჩანაწერში მარჯვნივ მდგომი მოქმედება პირველად სრულდება. დღეს მთლიანი მატრიცების გამრავლებას არ გამოვითვლით.

აქ ნაჩვენებია კონკრეტული საწინააღმდეგო მაგალითი. ეს არ ნიშნავს, რომ ნებისმიერი ორი მატრიცის რიგის შეცვლა ყოველთვის სხვადასხვა შედეგს იძლევა.

**Transition:** Use this result to introduce “ორი ვექტორიდან ვიღებთ ერთ ქულას”. The next scene begins from its opening state, with no preview of its result.

## 16. ორი ვექტორიდან ვიღებთ ერთ ქულას

- Duration: 21:30–23:30 (120 seconds).
- Objective: შემოვიტანოთ სკალარული ნამრავლი როგორც შეწონილი ჯამი.
- Central insight: ორი ვექტორიდან ვიღებთ ერთ ქულას
- Mathematical content: w · x = 2×3 + (−1)×1 = 5
- Composition, diagram and animation: Large component pairs feed two product terms, then combine into one dominant score.
- Exact construction: `visual_scenes.py`, `draw_dot()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/16.jpg`.

### Speaker notes

ვექტორების სკალარული ნამრავლი ასე ითვლება: შესაბამის კომპონენტებს ვამრავლებთ და შედეგებს ვკრებთ. პასუხი ერთი რიცხვია.

ავიღოთ w=(2,−1) და x=(3,1). პირველი წვლილია 6, მეორე — −1. ჯამი არის 5. უარყოფითი წონა შესაბამისი ნიშნის წვლილს ამცირებს.

მანქანურ სწავლაში x აღწერს მაგალითს, w კი შეიცავს წონებს. წონა აჩვენებს, როგორ მოქმედებს კონკრეტული ნიშანი ქულაზე, როცა სხვა ნიშნები უცვლელია.

სთხოვეთ აუდიტორიას გამოთვალოს იგივე წონებით x=(1,3). პასუხია −1. აღნიშნეთ, რომ ქულა თავისთავად ალბათობა არ არის.

**Transition:** Use this result to introduce “პროექციას აქვს სიდიდე და ნიშანი”. The next scene begins from its opening state, with no preview of its result.

## 17. პროექციას აქვს სიდიდე და ნიშანი

- Duration: 23:30–25:00 (90 seconds).
- Objective: დავაკავშიროთ სკალარული ნამრავლი პროექციასთან.
- Central insight: პროექციას აქვს სიდიდე და ნიშანი
- Mathematical content: w = (1, 0)     w · x = x₁
- Composition, diagram and animation: Full-frame projection; a dashed perpendicular and signed shadow follow the moving vector.
- Exact construction: `visual_scenes.py`, `draw_projection()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/17.jpg`.

### Speaker notes

ამჯერად w=(1,0), ანუ ერთეულოვანი ჰორიზონტალური ისარი. მისი სკალარული ნამრავლი x-თან უბრალოდ x-ის ჰორიზონტალურ კომპონენტს გვაძლევს.

წყვეტილი ხაზი აჩვენებს პროექციას: x=(2,1)-ისთვის პასუხია 2. x=(0,2)-ისთვის ნული, ხოლო x=(−2,1)-ისთვის −2.

ზოგადად სკალარული ნამრავლი დამოკიდებულია მიმართულებაზეც და სიგრძეებზეც. მხოლოდ ერთეულოვანი w-ის შემთხვევაში უდრის იგი მიმართულებიან პროექციის სიგრძეს. ამიტომ დიდი ქულა ყოველთვის უფრო მსგავს მიმართულებას არ ნიშნავს.

ჰკითხეთ, რატომ ქრება ვერტიკალური კომპონენტის წვლილი ამ კონკრეტულ მაგალითში.

**Transition:** Use this result to introduce “ქულა გვაძლევს კატეგორიას”. The next scene begins from its opening state, with no preview of its result.

## 18. ქულა გვაძლევს კატეგორიას

- Duration: 25:00–26:30 (90 seconds).
- Objective: დავაკავშიროთ ნიშნები, წონები, ქულა და კატეგორია.
- Central insight: ქულა გვაძლევს კატეგორიას
- Mathematical content: s = w · x + b = x₁ − x₂
- Composition, diagram and animation: Large labeled classification plane, a translucent decision partition and direct class labels.
- Exact construction: `visual_scenes.py`, `draw_classifier()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/18.jpg`.

### Speaker notes

დავუბრუნდეთ ხილს. ავიღოთ წონები w=(1,−1) და b=0. ქულა სიგანისა და სიმაღლის სხვაობაა. ჩვენი გამოგონილი წესი ამბობს: s≥0 — ვაშლი; s<0 — მსხალი.

აქ წესს ხელით ვირჩევთ, რათა მოქმედება გასაგები იყოს. ეს ჯერ ნასწავლი კლასიფიკატორი არ არის. რეალურ სწავლაში პარამეტრების შერჩევა მონაცემებს უნდა დაეყრდნოს.

კლასიფიკაცია ნიშნავს კატეგორიის არჩევას. არც ეს ორი ნიშანი და არც ეს ხაზი ყველა რეალურ ხილს საიმედოდ ვერ გაარჩევს. შეგვიძლია გვქონდეს მაღალი ვაშლი ან განიერი მსხალი.

გამოთვალეთ (3,2): ქულაა 1, ამიტომ წესი ირჩევს ვაშლს. (2,3)-ისთვის ქულაა −1 და პასუხია მსხალი.

**Transition:** Use this result to introduce “ნულოვანი ქულა ქმნის საზღვარს”. The next scene begins from its opening state, with no preview of its result.

## 19. ნულოვანი ქულა ქმნის საზღვარს

- Duration: 26:30–28:00 (90 seconds).
- Objective: ქულის ნული ვაჩვენოთ გადაწყვეტილების საზღვრად.
- Central insight: ნულოვანი ქულა ქმნის საზღვარს
- Mathematical content: s = 0  →  x₂ = x₁
- Composition, diagram and animation: A point crosses the decision boundary while its score changes in place.
- Exact construction: `visual_scenes.py`, `draw_boundary()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/19.jpg`.

### Speaker notes

წესის პასუხი იქ იცვლება, სადაც ქულა ნულია. ჩვენი მაგალითისთვის x₁−x₂=0, ანუ x₁=x₂. ეს დიაგონალური წრფეა.

ხაზის ქვემოთ სიგანე მეტია სიმაღლეზე და ქულა დადებითია. ზემოთ ქულა უარყოფითია. თვითონ ხაზზე ჩვენი შეთანხმებით ვაშლს ვირჩევთ.

ჰკითხეთ, შეიცვლება თუ არა პასუხი, როცა წერტილი იმავე მხარეს მოძრაობს. ქულის სიდიდე შეიცვლება, მაგრამ კატეგორია აუცილებელი არ არის შეიცვალოს.

**Transition:** Use this result to introduce “თავისუფალი წევრი წევს საზღვარს”. The next scene begins from its opening state, with no preview of its result.

## 20. თავისუფალი წევრი წევს საზღვარს

- Duration: 28:00–29:30 (90 seconds).
- Objective: ავხსნათ b-ის როლი და წრფივ/აფინურ გარდაქმნებს შორის განსხვავება.
- Central insight: თავისუფალი წევრი წევს საზღვარს
- Mathematical content: s = x₁ − x₂ + b
- Composition, diagram and animation: Parallel boundary motion tied to a changing bias value; a stationary point changes side.
- Exact construction: `visual_scenes.py`, `draw_bias()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/20.jpg`.

### Speaker notes

b-ს თავისუფალი წევრი, ან bias, ეწოდება. თუ b=1, ნულოვანი ქულის საზღვარია x₂=x₁+1. მისი დახრილობა უცვლელია, მდებარეობა კი იცვლება.

წონები საზღვრის მიმართულებას უკავშირდება, თავისუფალი წევრი კი მის გადაწევას. აჩვენეთ წერტილი, რომლის პასუხიც ამ გადაწევამ შეცვალა.

ზუსტი მათემატიკური ტერმინით Wx+b არის აფინური გარდაქმნა; b=0-ის შემთხვევაში წრფივია. მანქანურ სწავლაში ასეთ მოდელებს ხშირად მაინც წრფივ მოდელებს უწოდებენ. ტერმინის განსხვავება აღნიშნეთ მოკლედ.

**Transition:** Use this result to introduce “მატრიცა ითვლის რამდენიმე ქულას”. The next scene begins from its opening state, with no preview of its result.

## 21. მატრიცა ითვლის რამდენიმე ქულას

- Duration: 29:30–31:00 (90 seconds).
- Objective: შევკრათ მატრიცისა და სკალარული ნამრავლის ორი ხედვა.
- Central insight: მატრიცა ითვლის რამდენიმე ქულას
- Mathematical content: Wx = [3, −3]   როცა x = (4, 1)
- Composition, diagram and animation: Two weight rows consume the same input and send results into two score bars.
- Exact construction: `visual_scenes.py`, `draw_scores()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/21.jpg`.

### Speaker notes

მატრიცის თითოეული სტრიქონი შეიძლება ცალკე წონის ვექტორი იყოს. პირველი სტრიქონი იყოს (1,−1), მეორე — (−1,1).

შეყვანისთვის (4,1) პირველი ქულაა 3, მეორე — −3. Wx ერთდროულად გვაძლევს ორივე სკალარულ ნამრავლს.

ამ მაგალითში უფრო დიდ ქულას ვირჩევთ. ეს ქულები ალბათობები არ არის და მათი ჯამი 1 არ უნდა იყოს. მატრიცა არის მრავალი მსგავსი გამოთვლის შეკრული ჩანაწერი.

**Transition:** Use this result to introduce “სტრიქონები სხვადასხვა მაგალითია”. The next scene begins from its opening state, with no preview of its result.

## 22. სტრიქონები სხვადასხვა მაგალითია

- Duration: 31:00–32:30 (90 seconds).
- Objective: განვასხვაოთ მონაცემის სტრიქონები და ნიშნის სვეტები.
- Central insight: სტრიქონები სხვადასხვა მაგალითია
- Mathematical content: X: 3×2     Wᵀ: 2×2     XWᵀ: 3×2
- Composition, diagram and animation: Three data rows and two weight columns feed a result matrix; row/column highlights show one actual multiplication.
- Exact construction: `visual_scenes.py`, `draw_batch()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/22.jpg`.

### Speaker notes

სამი მაგალითის ვექტორები X-ში სტრიქონებად ჩავწეროთ: (3,1), (1,3), (2,2). სამი სტრიქონი ნიშნავს სამ მაგალითს, ორი სვეტი — ორ ნიშანს.

აქ თითოეული x სტრიქონადაა შენახული. ამიტომ ქულების ცხრილს ვწერთ XWᵀ. ზედა T ნიშნავს ტრანსპონირებას: სტრიქონები და სვეტები ადგილებს ცვლიან.

შედეგი არის სამი სტრიქონი და ორი ქულა თითო სტრიქონში: (2,−2), (−2,2), (0,0). ტოლი ქულებისთვის ცალკე შეთანხმება გვჭირდება.

ამ ეტაპზე მთავარი ფორმაა: შიდა ზომები უნდა ემთხვეოდეს. ნუ მოსთხოვთ მთლიანი წესის დაზეპირებას.

ამ სპეციალურ მაგალითში W სიმეტრიულია, ამიტომ Wᵀ=W და ჩანაწერში რიცხვები არ იცვლება. ზოგადი მატრიცისთვის ტრანსპონირება ნამდვილად ცვლის სტრიქონებსა და სვეტებს.

**Transition:** Use this result to introduce “სწავლისას ვცვლით პარამეტრებს”. The next scene begins from its opening state, with no preview of its result.

## 23. სწავლისას ვცვლით პარამეტრებს

- Duration: 32:30–34:30 (120 seconds).
- Objective: სწავლა ავხსნათ პროგნოზისა და სწორი პასუხის შედარებით.
- Central insight: სწავლისას ვცვლით პარამეტრებს
- Mathematical content: b: −2 → −1 → 0; შეცდომები: 1/6 → 0/6 → 0/6
- Composition, diagram and animation: A moving boundary highlights mistakes and updates the error count at each discrete parameter choice.
- Exact construction: `visual_scenes.py`, `draw_training()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/23.jpg`.

### Speaker notes

დასაწყისში მოდელს შეიძლება ცუდი წონები ჰქონდეს. ვადარებთ მის პასუხებს ცნობილ კატეგორიებს და ვიღებთ შეცდომის საზომს. მერე პარამეტრებს ვცვლით.

ანიმაციაში საზღვარი წინასწარ შერჩეული ნაბიჯებით მოძრაობს; ეს სასწავლო დემონსტრაციაა და არა აქ გაშვებული ოპტიმიზაციის ალგორითმი.

რეალური ალგორითმი იყენებს დანაკარგის ფუნქციას და მისი შემცირების წესს. დღეს არც წარმოებული გვჭირდება, არც კონკრეტული ოპტიმიზატორის ფორმულა.

ცვლილება ყოველთვის გაუმჯობესებას არ იძლევა. ხელახლა უნდა გავზომოთ შედეგი. სთხოვეთ მოსწავლეებს მიუთითონ, რომელი წერტილის პასუხი შეიცვალა და რატომ.

**Transition:** Use this result to introduce “შეცდომის კვადრატი ზომავს აცდენას”. The next scene begins from its opening state, with no preview of its result.

## 24. შეცდომის კვადრატი ზომავს აცდენას

- Duration: 34:30–36:00 (90 seconds).
- Objective: დანაკარგის იდეა მარტივ რიცხვით მაგალითზე ვაჩვენოთ.
- Central insight: შეცდომის კვადრატი ზომავს აცდენას
- Mathematical content: L = ((ŷ₁−y₁)² + (ŷ₂−y₂)²) / 2
- Composition, diagram and animation: Two residual segments become squares of areas 1 and 4; their average is constructed visibly.
- Exact construction: `visual_scenes.py`, `draw_loss()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/24.jpg`.

### Speaker notes

ერთი წუთით კატეგორიებიდან რიცხვის პროგნოზზე გადავიდეთ. მაგალითად, შეიძლება ვცდილობდეთ ნივთის მასის პროგნოზს. ორი სწორი პასუხი იყოს 3 და 3; პროგნოზები — 2 და 5.

შეცდომებია −1 და 2. მათი კვადრატებია 1 და 4, საშუალო კი 2.5. ასე დიდ შეცდომას მეტი წვლილი აქვს, ხოლო დადებითი და უარყოფითი შეცდომები ერთმანეთს არ აუქმებს.

ეს საშუალო კვადრატული შეცდომაა, რიცხვითი პროგნოზის გავრცელებული საზომი. კლასიფიკაციისთვის ხშირად სხვა დანაკარგს იყენებენ. ჩვენი წინა კლასიფიკატორისთვის მას ავტომატურად არ ვირჩევთ.

ნახატზე თეთრი წერტილი სწორი მნიშვნელობაა, ცისფერი — პროგნოზი. კვადრატების გვერდების შეფარდება 1:2-ია, ამიტომ ფართობების შეფარდება 1:4 გამოდის.

**Transition:** Use this result to introduce “ახალი მაგალითები ამოწმებს წესს”. The next scene begins from its opening state, with no preview of its result.

## 25. ახალი მაგალითები ამოწმებს წესს

- Duration: 36:00–37:30 (90 seconds).
- Objective: ავხსნათ განზოგადება და შეფასებისთვის ახალი მონაცემების საჭიროება.
- Central insight: ახალი მაგალითები ამოწმებს წესს
- Mathematical content: სასწავლო მონაცემები ≠ ახალი მონაცემები
- Composition, diagram and animation: Known training examples remain fixed while newly outlined examples arrive, including two errors.
- Exact construction: `visual_scenes.py`, `draw_generalization()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/25.jpg`.

### Speaker notes

თუ მოდელმა ნანახ მაგალითებზე კარგი პასუხი მოგვცა, ეს ჯერ არ ნიშნავს, რომ ახალ შემთხვევებზეც კარგად იმუშავებს. შეიძლება შემთხვევითი თავისებურებები დაიმახსოვრა.

ამიტომ მაგალითების ნაწილს სწავლისგან ცალკე ვინახავთ და შედეგს მათზეც ვამოწმებთ. მოდელს სწავლისას ამ პასუხებზე წვდომა არ უნდა ჰქონდეს.

მონაცემები რეალურ ამოცანას უნდა ჰგავდეს. მხოლოდ პატარა ვაშლებზე სწავლა და მხოლოდ დიდ ვაშლებზე გამოყენება შეიძლება პრობლემური იყოს.

ჰკითხეთ: რატომ არ კმარა ტესტის სწორი პასუხების დამახსოვრება იმის დასამტკიცებლად, რომ თემა გავიგეთ? ანალოგია მოკლედ დააკავშირეთ მოდელთან.

**Transition:** Use this result to introduce “ქსელის ფენა აერთიანებს წონიან ჯამებს”. The next scene begins from its opening state, with no preview of its result.

## 26. ქსელის ფენა აერთიანებს წონიან ჯამებს

- Duration: 37:30–39:00 (90 seconds).
- Objective: ნეირონული ფენა უკვე ნასწავლ მოქმედებებთან დავაკავშიროთ.
- Central insight: ქსელის ფენა აერთიანებს წონიან ჯამებს
- Mathematical content: z = Wx + b
- Composition, diagram and animation: A large layered network introduction resolves into the actual 2→3 example; pulses trace weighted contributions and outputs.
- Exact construction: `visual_scenes.py`, `draw_network()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/26.jpg`.

### Speaker notes

ნეირონული ქსელის სახელმა არ შეგვაშინოს. ერთ ფენაში რამდენიმე შეწონილი ჯამი გამოითვლება. თითოეულ მათგანს თავისი წონები და თავისუფალი წევრი აქვს.

ორი შეყვანისა და სამი გამოსავლისთვის W არის 3×2 მატრიცა, b კი სამი რიცხვის ვექტორი. აქ ხაზები გამრავლების კავშირებს აღნიშნავს.

ჩვენს მაგალითში x=(2,1), მატრიცის სტრიქონებია (1,0), (0,1), (1,−1), ხოლო b=0. შედეგია (2,1,1). ეს ბიოლოგიური ტვინის ზუსტი მოდელი არ არის.

პირველი დიდი ქსელი მხოლოდ სტრუქტურის სქემაა: ფერები და წრის შევსება გაზომილი ალბათობები არ არის. შემდეგ კადრზე ზუსტად გამოთვლილ 2→3 მაგალითზე გადავდივართ. გამოტოვებული კავშირების წონა ნულია; მწვანე კავშირია +1, წითელი −1.

**Transition:** Use this result to introduce “ReLU ნულავს უარყოფით მნიშვნელობებს”. The next scene begins from its opening state, with no preview of its result.

## 27. ReLU ნულავს უარყოფით მნიშვნელობებს

- Duration: 39:00–40:30 (90 seconds).
- Objective: ავხსნათ მარტივი აქტივაცია და მხოლოდ წრფივი ფენების შეზღუდვა.
- Central insight: ReLU ნულავს უარყოფით მნიშვნელობებს
- Mathematical content: ReLU(z) = max(0, z)
- Composition, diagram and animation: A large ReLU graph and three moving values connect input to the clipped output.
- Exact construction: `visual_scenes.py`, `draw_relu()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/27.jpg`.

### Speaker notes

ხშირად ფენის შემდეგ არაწრფივ მოქმედებას ვასრულებთ. ReLU უარყოფით რიცხვს ნულით ცვლის, დადებითს კი უცვლელად ტოვებს.

თუ გვაქვს (−2,1,3), შედეგია (0,1,3). გრაფიკს ნულთან კუთხე აქვს. ეს არ არის ერთი სწორი ხაზი მთელ სიბრტყეზე.

მხოლოდ აფინური ფენების ერთმანეთზე მიყოლება ისევ ერთ აფინურ მოქმედებად შეიკვრება. არაწრფივი აქტივაციები ქსელს უფრო რთული დამოკიდებულებების აღწერის საშუალებას აძლევს.

დღეს ქსელს არ ვწვრთნით. მიზანია ამოვიცნოთ ნაცნობი ნაწილი: ვექტორი, მატრიცა, შეწონილი ჯამი და ახალი მარტივი ფუნქცია.

**Transition:** Use this result to introduce “გამოიყენეთ ყველაფერი ერთად”. The next scene begins from its opening state, with no preview of its result.

## 28. გამოიყენეთ ყველაფერი ერთად

- Duration: 40:30–42:30 (120 seconds).
- Objective: მოსწავლემ დამოუკიდებლად დააკავშიროს ნიშნები, სკალარული ნამრავლი და გადაწყვეტილება.
- Central insight: გამოიყენეთ ყველაფერი ერთად
- Mathematical content: x = (2, 3)     w = (1, −1)     b = 2
- Composition, diagram and animation: A full-scale challenge with its data, boundary task, and three short prompts; no answer.
- Exact construction: `visual_scenes.py`, `draw_quiz()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/28.jpg`.

### Speaker notes

30 წამი დაუთმეთ პირობას: x აღწერს ხილს, წონებია (1,−1), თავისუფალი წევრი — 2. წესი ისევ s≥0-ისას ვაშლს ირჩევს.

45 წამი ინდივიდუალური მუშაობისთვის: გამოთვალეთ s; აირჩიეთ კატეგორია; თქვით, რა შეიცვლება, თუ სიმაღლე 3-დან 5-მდე გაიზრდება.

30 წამი წყვილებში პასუხების შესადარებლად და 15 წამი ხელის აწევით შესაჯამებლად. სურვილისამებრ ჰკითხეთ ძლიერ მოსწავლეებს, როგორია ახალი საზღვრის განტოლება.

**Audience task:** 1. რა არის s?  2. რომელი კატეგორია?  3. თუ x=(2,5)?

**Expected answer:** s=1 → ვაშლი; ახალი s=−1 → მსხალი; საზღვარი x₂=x₁+2.

**Transition:** Use this result to introduce “საზღვრის გადაკვეთა ცვლის პასუხს”. The next scene begins from its opening state, with no preview of its result.

## 29. საზღვრის გადაკვეთა ცვლის პასუხს

- Duration: 42:30–43:30 (60 seconds).
- Objective: საბოლოო გამოთვლა გავარჩიოთ და შეცდომები შევასწოროთ.
- Central insight: საზღვრის გადაკვეთა ცვლის პასუხს
- Mathematical content: 2 − 3 + 2 = 1     →     ვაშლი
- Composition, diagram and animation: Two points on opposite sides of the shifted boundary resolve the challenge.
- Exact construction: `visual_scenes.py`, `draw_quiz_answer()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/29.jpg`.

### Speaker notes

თავდაპირველი ქულაა 2−3+2=1, ამიტომ შეთანხმებული წესი ირჩევს ვაშლს. გაზრდილი სიმაღლისთვის მივიღებთ 2−5+2=−1-ს და პასუხია მსხალი.

თუ ვინმემ თავისუფალი წევრი ორივე კოორდინატს დაუმატა, აჩვენეთ, რომ აქ b ერთ საბოლოო ქულას ერთხელ ემატება.

ჰკითხეთ მოსწავლეებს, რისი ახსნა შეუძლიათ ახლა ნახატით. სწორი პასუხი კარგია, მაგრამ განსაკუთრებით მნიშვნელოვანია, როგორ უკავშირდება გამოთვლა საზღვრის ორ მხარეს.

**Transition:** Use this result to introduce “რიცხვებიდან პროგნოზამდე”. The next scene begins from its opening state, with no preview of its result.

## 30. რიცხვებიდან პროგნოზამდე

- Duration: 43:30–45:00 (90 seconds).
- Objective: შევაჯამოთ ცოდნა და დავტოვოთ კითხვებისთვის დრო.
- Central insight: რიცხვებიდან პროგნოზამდე
- Mathematical content: ვექტორი → მატრიცა → ქულა → პროგნოზი
- Composition, diagram and animation: Four mathematical miniatures, not four text boxes, recap vectors, transformations, scores, and predictions.
- Exact construction: `visual_scenes.py`, `draw_recap()`; all coordinates, weights and transformation matrices are explicit.
- Color semantics: the global system above; labels and matrix entries match their geometric components.
- Playback: progressive construction, meaningful transformations, and a held result. Right arrow finishes this scene; the next right arrow advances. R replays; P permits an intermediate pause.
- Static alternative: `posters/30.jpg`.

### Speaker notes

ვექტორი აღწერს მაგალითს. მატრიცა გარდაქმნის ვექტორს ან რამდენიმე ქულას ითვლის. წონები და თავისუფალი წევრი მოდელის პარამეტრებია; სწავლა მათ მონაცემების მიხედვით ცვლის.

ჩვენ ავაგეთ პატარა გამოთვლა და გავიგეთ მისი გეომეტრია. ეს მანქანური სწავლების მხოლოდ საწყისი ნაწილია. შემდეგ შეხვედრაზე შეგვიძლია რეალური მონაცემები ჩავტვირთოთ და იგივე მოქმედებები Python-ით შევასრულოთ.

ბოლო წუთი დაუთმეთ კითხვებს და გასასვლელ პასუხს: ერთ წინადადებაში ახსენით, რით განსხვავდება მონაცემის ვექტორი წონის ვექტორისგან. ორივე რიცხვების სიაა, მაგრამ სხვადასხვა როლი აქვს.

**Transition:** Invite questions and the one-sentence exit answer from the notes.

## References

- [3Blue1Brown — linear transformations](https://www.3blue1brown.com/lessons/linear-transformations/)
- [3Blue1Brown — dot products](https://www.3blue1brown.com/lessons/dot-products/)
- [3Blue1Brown — video source reference](https://github.com/3b1b/videos)
- [Google — linear regression](https://developers.google.com/machine-learning/crash-course/linear-regression)
- [Google — activation functions](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions)
- [Manim Slides](https://manim-slides.eertmans.be/latest/)