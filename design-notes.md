# Redesign: a visual mathematics lecture

Format: an animated Georgian lesson, 30 presenter-controlled scenes, 45-minute teaching schedule.

The requested taste skill is applied to the slide compositions: one dominant subject per screen, equal safe margins, a fixed typography and spacing system, restrained copy, visible mathematical work at large scale, purposeful motion, and visual checks of the actual renders. Its business-site dealer, sales sections, photography counts, and website-only layout gate do not apply to a Manim lecture. This is not represented as a website gate pass.

## Reference study
- User-supplied screenshots: full-frame coordinate planes, basis vectors with persistent colors, algebra close to its geometric objects, parallel before/after transformation views, and network connections that show propagation.
- [3Blue1Brown linear transformations](https://www.3blue1brown.com/lessons/linear-transformations/): maintain a reference grid while transforming the working grid; connect basis-vector destinations to matrix columns.
- [Chapter 3 source](https://github.com/3b1b/videos/blob/master/_2016/eola/chapter3.py): inspected scene organization, progressive construction, and matrix-column/geometric correspondence.
- [Neural-network source](https://github.com/3b1b/videos/blob/master/_2017/nn/part1.py): inspected layers, edges, activation display and propagation concepts.
- The new implementation is original ManimCE code. Reference code, characters, footage, and logos are not copied.

## Visual system
- Almost-black ground #06090C. Subdued blue grid #1B4A5D. Warm-white type #F4F3EE.
- First vector/component green #8DD78A; second red #F17881; result yellow #F4DC6B; data/neutral input blue #59C5E8. Class markers distinguish categories by shape as well as color.
- Noto Sans Georgian for Georgian text, Cambria for mathematical notation. Noto is bundled under the SIL Open Font License. Latin characters and numerals in mixed Georgian prose use Segoe UI to align their baselines; mathematical expressions use Cambria Math. Rendering uses ManimCE 0.21.0 with Manim Slides 5.7.0; the offline HTML export needs no installation to present.
- Safe text margins 0.6 Manim units. Titles 30 px, major math 42–58 px, object labels 25–30 px. Geometry may intentionally bleed to screen edges; text never does.
- No universal title/rule/small-plot/right-paragraph/footer layout. No repeated explanatory caption under the visualization. Equations are part of the mathematical construction and labels sit near the relevant object.
- Smooth 2–4 second geometric transformations, sequential component reveals, and pauses at the result. No decorative loops or random flashing.

## Scene compositions and motion
01. Large title beside a full-height changing basis and translucent parallelogram.
02. Labeled examples form two clusters; a boundary and an unseen point establish the prediction question.
03. Large fruit silhouette, width/height measurement lines, then a color-linked column vector.
04. Full-frame plane; horizontal and vertical components lead to a large vector; coordinate matrix remains beside its endpoint.
05. Full-frame tip-to-tail addition, ghost arrows, and a highlighted resultant.
06. Full-frame scalar multiplication; the multiplier and vector change together while previous states leave a faint reference.
07. Full-frame basis exercise with a large unanswered linear combination.
08. Repeated basis steps resolve to one vector and a color-linked matrix equation.
09. Several multiples lie on one bright line; an unreachable point sits visibly off it.
10. A large input vector and matrix accompany a live grid stretch.
11. Equal before/after planes, translucent unit cells, and several tracked points show horizontal stretch.
12. Basis arrows shear with the grid, then their coordinates become matrix columns; a vector is assembled from those columns.
13. Large matrix question with a geometric reference and no answer.
14. Full-frame answer construction with color-linked column terms beside the geometry.
15. Two geometric routes show stretch/rotation in different orders, preserving the original vector as a ghost.
16. Large component pairs feed two product terms, then combine into one dominant score.
17. Full-frame projection; a dashed perpendicular and signed shadow follow the moving vector.
18. Large labeled classification plane, a translucent decision partition and direct class labels.
19. A point crosses the decision boundary while its score changes in place.
20. Parallel boundary motion tied to a changing bias value; a stationary point changes side.
21. Two weight rows consume the same input and send results into two score bars.
22. Three data rows and two weight columns feed a result matrix; row/column highlights show one actual multiplication.
23. A moving boundary highlights mistakes and updates the error count at each discrete parameter choice.
24. Two residual segments become squares of areas 1 and 4; their average is constructed visibly.
25. Known training examples remain fixed while newly outlined examples arrive, including two errors.
26. A large layered network introduction resolves into the actual 2→3 example; pulses trace weighted contributions and outputs.
27. A large ReLU graph and three moving values connect input to the clipped output.
28. A full-scale challenge with its data, boundary task, and three short prompts; no answer.
29. Two points on opposite sides of the shifted boundary resolve the challenge.
30. Four mathematical miniatures, not four text boxes, recap vectors, transformations, scores, and predictions.

## Verification
Render every scene, review contact sheets and full-size frames, check intermediate transformation frames and text bounds, verify all MP4s and opening posters, then test the actual Manim Slides export: first right arrow finishes and holds; second advances; replay resets; rapid navigation and delayed loading never show a future final frame. Verify the private presenter window. The detailed results are recorded in verification.md.
