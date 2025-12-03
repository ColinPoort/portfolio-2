
content = """
1: <!DOCTYPE html>
2: <html lang="nl">
3: 
4: <head>
5:     <meta charset="UTF-8">
6:     <meta name="viewport" content="width=device-width, initial-scale=1.0">
7:     <title>Colin Poort — Software Developer / Crafting Modern Web Solutions</title>
8:     <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"
9:         rel="stylesheet">
10:     <style>
11:         * {
12:             margin: 0;
13:             padding: 0;
14:             box-sizing: border-box;
15:         }
16: 
17:         :root {
18:             --primary-bg: #0a0a0a;
19:             --secondary-bg: #141414;
20:             --accent-color: #3b82f6;
21:             --text-primary: #ffffff;
22:             --text-secondary: #a3a3a3;
23:             --card-bg: #1a1a1a;
24:         }
25: 
26:         body {
27:             font-family: 'Poppins', sans-serif;
28:             background-color: var(--primary-bg);
29:             color: var(--text-primary);
30:             line-height: 1.6;
31:             overflow-x: hidden;
32:         }
33: 
34:         html {
35:             scroll-behavior: smooth;
36:         }
37: 
38:         /* Navigation */
39:         nav {
40:             position: fixed;
41:             top: 0;
42:             width: 100%;
43:             background: rgba(10, 10, 10, 0.72);
44:             backdrop-filter: blur(10px);
45:             padding: 1.5rem 5%;
46:             display: flex;
47:             justify-content: space-between;
48:             align-items: center;
49:             z-index: 1000;
50:             transition: all 0.3s ease;
51:         }
52: 
53:         nav.scrolled {
54:             padding: 1rem 5%;
55:             background: rgba(10, 10, 10, 0.88);
56:             box-shadow: 0 2px 20px rgba(0, 0, 0, 0.5);
57:         }
58: 
59:         .logo {
60:             font-size: 1.5rem;
61:             font-weight: 700;
62:             color: var(--text-primary);
63:             text-decoration: none;
64:         }
65: 
66:         .nav-links {
67:             display: flex;
68:             gap: 2.5rem;
69:             list-style: none;
70:         }
71: 
72:         .nav-links a {
73:             color: var(--text-secondary);
74:             text-decoration: none;
75:             font-weight: 500;
76:             transition: color 0.3s ease;
77:             position: relative;
78:             display: inline-block;
79:         }
80: 
81:         .nav-links a::after {
82:             content: '';
83:             position: absolute;
84:             width: 0;
85:             height: 2px;
86:             bottom: -5px;
87:             left: 0;
88:             background-color: var(--accent-color);
89:             transition: width 0.3s ease;
90:         }
91: 
92:         .nav-links a:hover {
93:             color: var(--text-primary);
94:         }
95: 
96:         .nav-links a:hover::after {
97:             width: 100%;
98:         }
99: 
100:         .nav-links a span {
101:             display: inline-block;
102:             transition: transform 0.3s ease;
103:         }
104: 
105:         .nav-links a:hover span {
106:             animation: letterScroll 0.5s ease forwards;
107:         }
108: 
109:         @keyframes letterScroll {
110: 
111:             0%,
112:             100% {
113:                 transform: translateY(0);
114:             }
115: 
116:             50% {
117:                 transform: translateY(-5px);
118:             }
119:         }
120: 
121:         .contact-btn {
122:             padding: 0.7rem 1.5rem;
123:             background-color: transparent;
124:             border: 2px solid var(--accent-color);
125:             color: var(--text-primary);
126:             border-radius: 50px;
127:             cursor: pointer;
128:             transition: all 0.3s ease;
129:             font-weight: 500;
130:             text-decoration: none;
131:             display: inline-block;
132:         }
133: 
134:         .contact-btn:hover {
135:             background-color: var(--accent-color);
136:             transform: translateY(-2px);
137:             box-shadow: none;
138:         }
139: 
140:         /* Hero */
141:         .hero {
142:             min-height: 100vh;
143:             display: flex;
144:             align-items: center;
145:             justify-content: center;
146:             padding: 8rem 5% 5rem;
147:             position: relative;
148:             overflow: hidden;
149:             background-color: #000;
150:         }
151: 
152:         .hero-grid-container {
153:             position: absolute;
154:             top: 55%;
155:             left: 50%;
156:             width: 300vw;
157:             height: 300vh;
158:             transform: translate(-50%, -50%) scale(1);
159:             display: grid;
160:             grid-template-columns: repeat(3, 1fr);
161:             grid-template-rows: repeat(3, 1fr);
162:             transition: transform 0.1s ease-out;
163:             z-index: 0;
164:         }
165: 
166:         .hero-grid-item {
167:             width: 100%;
168:             height: 100%;
169:             overflow: hidden;
170:             position: relative;
171:             border: 10px solid rgba(0, 0, 0, 0.4);
172:         }
173: 
174:         .hero-grid-item img {
175:             width: 100%;
176:             height: 100%;
177:             object-fit: cover;
178:             display: block;
179:         }
180: 
181:         .hero-grid-item::after {
182:             content: '';
183:             position: absolute;
184:             top: 0;
185:             left: 0;
186:             right: 0;
187:             bottom: 0;
188:             background: rgba(0, 0, 0, 0.4);
189:             z-index: 1;
190:         }
191: 
192:         .hero-content {
193:             max-width: 900px;
194:             text-align: center;
195:             z-index: 10;
196:             position: relative;
197:             animation: fadeInUp 1s ease;
198:         }
199: 
200:         @keyframes fadeInUp {
201:             from {
202:                 opacity: 0;
203:                 transform: translateY(30px);
204:             }
205: 
206:             to {
207:                 opacity: 1;
208:                 transform: translateY(0);
209:             }
210:         }
211: 
212:         .hero h1 {
213:             font-size: 4rem;
214:             font-weight: 800;
215:             margin-bottom: 1.5rem;
216:             background: linear-gradient(135deg, #ffffff 0%, #3b82f6 100%);
217:             -webkit-background-clip: text;
218:             -webkit-text-fill-color: transparent;
219:             background-clip: text;
220:             line-height: 1.2;
221:         }
222: 
223:         .hero p {
224:             font-size: 1.3rem;
225:             color: var(--text-secondary);
226:             margin-bottom: 2.5rem;
227:             max-width: 700px;
228:             margin-left: auto;
229:             margin-right: auto;
230:         }
231: 
232:         .cta-button {
233:             display: inline-flex;
234:             align-items: center;
235:             gap: 1rem;
236:             padding: 1rem 2.5rem;
237:             background-color: var(--accent-color);
238:             color: var(--text-primary);
239:             text-decoration: none;
240:             border-radius: 50px;
241:             font-weight: 600;
242:             font-size: 1.1rem;
243:             transition: all 0.3s ease;
244:             box-shadow: none;
245:         }
246: 
247:         .cta-button:hover {
248:             transform: translateY(-3px);
249:             box-shadow: none;
250:         }
251: 
252:         .cta-button svg {
253:             width: 20px;
254:             height: 20px;
255:             transition: transform 0.3s ease;
256:         }
257: 
258:         .cta-button:hover svg {
259:             transform: translateX(5px);
260:         }
261: 
262:         /* Sections */
263:         .about {
264:             padding: 8rem 5%;
265:             background-color: var(--secondary-bg);
266:             position: relative;
267:             overflow: hidden;
268:             border-top: 1px solid rgba(255, 255, 255, 0.06);
269:             background-image: linear-gradient(to bottom, rgba(255, 255, 255, 0.06) 0 1px, transparent 1px), linear-gradient(to right, rgba(255, 255, 255, 0.06) 0 1px, transparent 1px);
270:             background-size: 100% 64px, 64px 100%;
271:         }
272: 
273:         .about::before {
274:             content: none;
275:         }
276: 
277:         .about-constellation {
278:             position: absolute;
279:             inset: 0;
280:             pointer-events: none;
281:             opacity: 0.25;
282:         }
283: 
284:         .about-constellation svg {
285:             width: 100%;
286:             height: 100%;
287:             display: block;
288:         }
289: 
290:         .about-constellation g {
291:             animation: drift 24s ease-in-out infinite alternate;
292:         }
293: 
294:         .about-constellation .star {
295:             fill: rgba(255, 255, 255, 0.8);
296:             transform-origin: center;
297:             animation: twinkle 3.2s ease-in-out infinite;
298:         }
299: 
300:         .about-constellation .line {
301:             stroke: rgba(255, 255, 255, 0.18);
302:             stroke-width: 2;
303:             stroke-linecap: round;
304:             stroke-dasharray: 140;
305:             stroke-dashoffset: 140;
306:             animation: draw 2.2s ease forwards;
307:         }
308: 
309:         .about-constellation .line:nth-of-type(1) {
310:             animation-delay: 0.1s;
311:         }
312: 
313:         .about-constellation .line:nth-of-type(2) {
314:             animation-delay: 0.3s;
315:         }
316: 
317:         .about-constellation .line:nth-of-type(3) {
318:             animation-delay: 0.5s;
319:         }
320: 
321:         .about-constellation .line:nth-of-type(4) {
322:             animation-delay: 0.7s;
323:         }
324: 
325:         .about-constellation .line:nth-of-type(5) {
326:             animation-delay: 0.9s;
327:         }
328: 
329:         .about-constellation .line:nth-of-type(6) {
330:             animation-delay: 1.1s;
331:         }
332: 
333:         .about-constellation .line:nth-of-type(7) {
334:             animation-delay: 1.3s;
335:         }
336: 
337:         .about-constellation .line:nth-of-type(8) {
338:             animation-delay: 1.5s;
339:         }
340: 
341:         .about-constellation .line:nth-of-type(9) {
342:             animation-delay: 1.7s;
343:         }
344: 
345:         .about-constellation .line:nth-of-type(10) {
346:             animation-delay: 1.9s;
347:         }
348: 
349:         .about-constellation .line:nth-of-type(11) {
350:             animation-delay: 2.1s;
351:         }
352: 
353:         .about-constellation .star:nth-of-type(odd) {
354:             animation-duration: 3.6s;
355:             animation-delay: 0.4s;
356:         }
357: 
358:         .about-constellation .star:nth-of-type(3n) {
359:             animation-duration: 2.8s;
360:             animation-delay: 0.2s;
361:         }
362: 
363:         @keyframes twinkle {
364: 
365:             0%,
366:             100% {
367:                 opacity: 0.7;
368:                 transform: scale(0.98);
369:             }
370: 
371:             50% {
372:                 opacity: 1;
373:                 transform: scale(1.02);
374:             }
375:         }
376: 
377:         @keyframes draw {
378:             to {
379:                 stroke-dashoffset: 0;
380:             }
381:         }
382: 
383:         @keyframes drift {
384:             0% {
385:                 transform: translateY(-3px) translateX(0);
386:             }
387: 
388:             100% {
389:                 transform: translateY(3px) translateX(6px);
390:             }
391:         }
392: 
393:         @media (prefers-reduced-motion: reduce) {
394:             .about-constellation g {
395:                 animation: none;
396:             }
397: 
398:             .about-constellation .star {
399:                 animation: none;
400:             }
401: 
402:             .about-constellation .line {
403:                 animation: none;
404:                 stroke-dashoffset: 0;
405:             }
406:         }
407: 
408:         .section-title {
409:             font-size: 2.5rem;
410:             font-weight: 700;
411:             margin-bottom: 1rem;
412:             text-align: center;
413:         }
414: 
415:         .section-subtitle {
416:             text-align: center;
417:             color: var(--text-secondary);
418:             font-size: 1.1rem;
419:             max-width: 600px;
420:             margin: 0 auto 4rem;
421:         }
422: 
423:         .about-content {
424:             max-width: 1200px;
425:             margin: 0 auto;
426:             position: relative;
427:             z-index: 1;
428:         }
429: 
430:         .about-main-card {
431:             background: linear-gradient(135deg, var(--card-bg) 0%, #1f1f1f 100%);
432:             border-radius: 30px;
433:             padding: 4rem;
434:             margin-bottom: 3rem;
435:             box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
436:             border: 1px solid rgba(59, 130, 246, 0.1);
437:             position: relative;
438:             overflow: hidden;
439:             border-left: 4px solid rgba(59, 130, 246, 0.35);
440:         }
441: 
442:         .about-main-card::before {
443:             content: none;
444:         }
445: 
446:         .about-flex {
447:             display: flex;
448:             gap: 4rem;
449:             align-items: center;
450:             position: relative;
451:             z-index: 1;
452:         }
453: 
454:         .about-text {
455:             flex: 1;
456:         }
457: 
458:         .about-text h3 {
459:             font-size: 2.5rem;
460:             margin-bottom: 1rem;
461:             background: linear-gradient(135deg, #ffffff 0%, #3b82f6 100%);
462:             -webkit-background-clip: text;
463:             -webkit-text-fill-color: transparent;
464:             background-clip: text;
465:         }
466: 
467:         .about-text .subtitle {
468:             color: var(--accent-color);
469:             font-size: 0.9rem;
470:             font-weight: 600;
471:             text-transform: uppercase;
472:             letter-spacing: 2px;
473:             margin-bottom: 1rem;
474:         }
475: 
476:         .about-text p {
477:             color: var(--text-secondary);
478:             font-size: 1.05rem;
479:             margin-bottom: 1.5rem;
480:             line-height: 1.9;
481:         }
482: 
483:         .about-image-wrapper {
484:             flex: 0 0 280px;
485:             position: relative;
486:         }
487: 
488:         .about-image {
489:             position: relative;
490:             border-radius: 20px;
491:             overflow: hidden;
492:             box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
493:             border: 1px solid rgba(255, 255, 255, 0.08);
494:         }
495: 
496:         .about-image img {
497:             width: 100%;
498:             height: 350px;
499:             object-fit: cover;
500:             display: block;
501:             transition: transform 0.5s ease;
502:         }
503: 
504:         .about-image:hover img {
505:             transform: scale(1.1);
506:         }
507: 
508:         .about-image::after {
509:             content: '';
510:             position: absolute;
511:             inset: 0;
512:             background: linear-gradient(180deg, transparent 0%, rgba(59, 130, 246, 0.2) 100%);
513:         }
514: 
515:         .about-stats {
516:             display: grid;
517:             grid-template-columns: repeat(3, 1fr);
518:             gap: 2rem;
519:         }
520: 
521:         .stat-card {
522:             background-color: var(--card-bg);
523:             padding: 2rem;
524:             border-radius: 20px;
525:             text-align: center;
526:             transition: all 0.3s ease;
527:             border: 1px solid transparent;
528:             position: relative;
529:             overflow: hidden;
530:         }
531: 
532:         .stat-card::before {
533:             content: '';
534:             position: absolute;
535:             inset: 0;
536:             background: linear-gradient(135deg, transparent 0%, rgba(59, 130, 246, 0.05) 100%);
537:             opacity: 0;
538:             transition: opacity 0.3s ease;
539:         }
540: 
541:         .stat-card:hover {
542:             transform: translateY(-5px);
543:             border-color: var(--accent-color);
544:             box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
545:         }
546: 
547:         .stat-card:hover::before {
548:             opacity: 1;
549:         }
550: 
551:         .stat-number {
552:             font-size: 2.5rem;
553:             font-weight: 800;
554:             color: var(--accent-color);
555:             margin-bottom: 0.5rem;
556:             position: relative;
557:         }
558: 
559:         .stat-label {
560:             color: var(--text-secondary);
561:             font-size: 0.95rem;
562:             font-weight: 500;
563:             position: relative;
564:         }
565: 
566:         /* Features */
567:         .features {
568:             padding: 8rem 5%;
569:             background-color: var(--primary-bg);
570:         }
571: 
572:         .features-grid {
573:             display: grid;
574:             grid-template-columns: repeat(3, 1fr);
575:             gap: 3rem;
576:             max-width: 1200px;
577:             margin: 0 auto;
578:         }
579: 
580:         .feature-card {
581:             background-color: var(--card-bg);
582:             padding: 3rem 2rem;
583:             border-radius: 20px;
584:             text-align: center;
585:             transition: all 0.3s ease;
586:             border: 1px solid transparent;
587:         }
588: 
589:         .feature-card:hover {
590:             transform: translateY(-10px);
591:             border-color: var(--accent-color);
592:             box-shadow: 0 20px 40px rgba(59, 130, 246, 0.2);
593:         }
594: 
595:         .feature-icon {
596:             width: 80px;
597:             height: 80px;
598:             margin: 0 auto 1.5rem;
599:         }
600: 
601:         .feature-icon img {
602:             width: 100%;
603:             height: 100%;
604:             object-fit: contain;
605:         }
606: 
607:         .feature-card h3 {
608:             font-size: 1.5rem;
609:             margin-bottom: 1rem;
610:         }
611: 
612:         .feature-card p {
613:             color: var(--text-secondary);
614:             line-height: 1.8;
615:         }
616: 
617:         .pro {
618:             padding: 8rem 5%;
619:             background-color: var(--primary-bg);
620:         }
621: 
622:         .pro-inner {
623:             max-width: 1200px;
624:             margin: 0 auto;
625:             display: grid;
626:             grid-template-columns: 1.1fr 0.9fr;
627:             gap: 3rem;
628:             align-items: start;
629:         }
630: 
631:         .pro-header h2 {
632:             font-size: 2.25rem;
633:             font-weight: 700;
634:             letter-spacing: 0.2px;
635:         }
636: 
637:         .pro-header p {
638:             margin-top: 0.75rem;
639:             color: var(--text-secondary);
640:             max-width: 56ch;
641:         }
642: 
643:         .pro-cards {
644:             display: grid;
645:             grid-template-columns: 1fr 1fr;
646:             gap: 1.5rem;
647:         }
648: 
649:         .pro-card {
650:             background: linear-gradient(135deg, var(--card-bg) 0%, #1f1f1f 100%);
651:             border: 1px solid rgba(255, 255, 255, 0.08);
652:             border-radius: 16px;
653:             padding: 1.5rem;
654:             transition: border-color 0.25s ease, box-shadow 0.25s ease;
655:         }
656: 
657:         .pro-card:hover {
658:             border-color: rgba(59, 130, 246, 0.35);
659:             box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
660:         }
661: 
662:         .pro-card h3 {
663:             font-size: 1.1rem;
664:             font-weight: 600;
665:             margin-bottom: 0.5rem;
666:             letter-spacing: 0.2px;
667:         }
668: 
669:         .pro-card p {
670:             color: var(--text-secondary);
671:             line-height: 1.8;
672:         }
673: 
674:         .pro-list {
675:             display: grid;
676: 
677:             .pro-aside {
678:                 display: grid;
679:                 gap: 1.5rem;
680:             }
681: 
682:             .pro-cta {
683:                 filter: brightness(0) invert(1);
684:             }
685: 
686:             /* Responsive */
687:             @media (max-width: 1024px) {
688:                 .hero h1 {
689:                     font-size: 3rem;
690:                 }
691: 
692:                 .about-content {
693:                     gap: 3rem;
694:                 }
695: 
696:                 .features-grid {
697:                     grid-template-columns: repeat(2, 1fr);
698:                 }
699: 
700:                 .projects-grid {
701:                     grid-template-columns: repeat(2, 1fr);
702:                 }
703: 
704:                 .pro-inner {
705:                     grid-template-columns: 1fr;
706:                 }
707: 
708:                 .pro-cards {
709:                     grid-template-columns: 1fr 1fr;
710:                 }
711: 
712:                 .metrics {
713:                     grid-template-columns: repeat(3, 1fr);
714:                 }
715: 
716:                 .contact-inner {
717:                     grid-template-columns: 1fr;
718:                 }
719: 
720:                 .contact-cards {
721:                     grid-template-columns: 1fr 1fr;
722:                 }
723:             }
724: 
725:             @media (max-width: 768px) {
726:                 nav {
727:                     padding: 1rem 5%;
728:                 }
729: 
730:                 .nav-links {
731:                     display: none;
732:                 }
733: 
734:                 .hero {
735:                     padding: 6rem 5% 4rem;
736:                 }
737: 
738:                 .hero h1 {
739:                     font-size: 2.5rem;
740:                 }
741: 
742:                 .hero p {
743:                     font-size: 1rem;
744:                 }
745: 
746:                 .cta-button {
747:                     font-size: 1rem;
748:                     padding: 0.9rem 2rem;
749:                 }
750: 
751:                 .about-content,
752:                 .features-grid,
753:                 .contact-info {
754:                     grid-template-columns: 1fr;
755:                     gap: 2rem;
756:                 }
757: 
758:                 .projects-grid {
759:                     grid-template-columns: 1fr;
760:                     gap: 1.5rem;
761:                 }
762: 
763:                 .pro-cards {
764:                     grid-template-columns: 1fr;
765:                 }
766: 
767:                 .metrics {
768:                     grid-template-columns: repeat(3, 1fr);
769:                 }
770: 
771:                 .contact-cards {
772:                     grid-template-columns: 1fr;
773:                 }
774: 
775:                 .form-row {
776:                     grid-template-columns: 1fr;
777:                 }
778: 
779:                 .about,
780:                 .features,
781:                 .projects,
782:                 .contact,
783:                 .cta-section {
784:                     padding: 5rem 5%;
785:                 }
786: 
787:                 .section-title {
788:                     font-size: 2rem;
789:                 }
790: 
791:                 .section-subtitle {
792:                     font-size: 1rem;
793:                 }
794: 
795:                 .cta-content h2 {
796:                     font-size: 2rem;
797:                 }
798: 
799:                 .cta-content p {
800:                     font-size: 1rem;
"""
