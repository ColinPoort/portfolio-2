
content += """
801:                 }
802: 
803:                 .footer-content {
804:                     flex-direction: column;
805:                     gap: 2rem;
806:                 }
807: 
808:                 .feature-card {
809:                     padding: 2rem 1.5rem;
810:                 }
811:             }
812: 
813:             @media (max-width: 480px) {
814:                 .hero h1 {
815:                     font-size: 2rem;
816:                 }
817: 
818:                 .section-title {
819:                     font-size: 1.75rem;
820:                 }
821: 
822:                 .cta-content h2 {
823:                     font-size: 1.75rem;
824:                 }
825:             }
826:     </style>
827: </head>
828: 
829: <body>
830:     <!-- Navigation -->
831:     <nav id="navbar">
832:         <a href="#home" class="logo">Colin Poort</a>
833:         <ul class="nav-links">
834:             <li><a href="#home">Home</a></li>
835:             <li><a href="#about">Over mij</a></li>
836:             <li><a href="#skills">Skills</a></li>
837:             <li><a href="#projects">Projecten</a></li>
838:         </ul>
839:         <a href="#contact" class="contact-btn">Contact</a>
840:     </nav>
841: 
842:     <!-- Hero Section -->
843:     <section class="hero" id="home">
844:         <div class="hero-grid-container" id="heroGrid">
845:             <div class="hero-grid-item"><img src="image/wmonster.png" alt="Gym"></div>
846:             <div class="hero-grid-item"><img src="image/lightweight.png" alt="Gym"></div>
847:             <div class="hero-grid-item"><img src="image/kendrick.png" alt="Gym"></div>
848:             <div class="hero-grid-item"><img src="image/kendrick2.png" alt="Gym"></div>
849:             <div class="hero-grid-item"><img src="image/IMG_6465.jpg" alt="Gym"></div>
850:             <div class="hero-grid-item"><img src="image/IMG_6464.jpg" alt="Gym"></div>
851:             <div class="hero-grid-item"><img src="image/IMG_6466.jpg" alt="Gym"></div>
852:             <div class="hero-grid-item"><img src="image/hangout.png" alt="Gym"></div>
853:             <div class="hero-grid-item"><img src="image/gym2.png" alt="Gym"></div>
854:         </div>
855:         <div class="hero-content">
856:             <h1>Crafting Modern Web Solutions</h1>
857:             <p>Welkom bij mijn portfolio, waar elke website een verhaal vertelt van innovatie en kwaliteit. Ontdek de
858:                 digitale wereld van webapplicaties, moderne interfaces en gebruiksvriendelijke oplossingen.</p>
859:             <a href="#projects" class="cta-button">
860:                 Bekijk Mijn Werk
861:                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" width="20" height="20">
862:                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6">
863:                     </path>
864:                 </svg>
865:             </a>
866:         </div>
867:     </section>
868: 
869:     <section class="pro" id="professional">
870:         <div class="pro-inner">
871:             <div class="pro-main">
872:                 <div class="pro-header">
873:                     <h2>Professional Services for Modern Web</h2>
874:                     <p>Ik ontwerp en ontwikkel snelle, toegankelijke en schaalbare weboplossingen. Met focus op nette
875:                         code, doordachte UX en consistente branding lever ik betrouwbare resultaten die bij jouw doelen
876:                         passen.</p>
877:                 </div>
878:                 <div class="pro-cards" style="margin-top:1.5rem;">
879:                     <div class="pro-card">
880:                         <h3>Design to Development</h3>
881:                         <p>Pixel-perfect implementaties van Figma/Sketch naar semantische, onderhoudbare front-ends.</p>
882:                         <ul class="pro-list">
883:                             <li>Responsief en toegankelijk (WCAG)</li>
884:                             <li>Component-gedreven architectuur</li>
885:                             <li>Performance-first (Lighthouse)</li>
886:                         </ul>
887:                     </div>
888:                     <div class="pro-card">
889:                         <h3>Web Applications</h3>
890:                         <p>Functionele applicaties met veilige dataflows en duidelijke interacties.</p>
891:                         <ul class="pro-list">
892:                             <li>Form handling en validatie</li>
893:                             <li>API-integraties</li>
894:                             <li>State management</li>
895:                         </ul>
896:                     </div>
897:                     <div class="pro-card">
898:                         <h3>Optimization & Refactor</h3>
899:                         <p>Opschonen, versnellen en verbeteren van bestaande codebases zonder regressies.</p>
900:                         <ul class="pro-list">
901:                             <li>Bundle- en image-optimalisatie</li>
902:                             <li>Toegankelijkheids-audits</li>
903:                             <li>Best practices & linting</li>
904:                         </ul>
905:                     </div>
906:                     <div class="pro-card">
907:                         <h3>Consult & Roadmap</h3>
908:                         <p>Heldere technische keuzes en roadmap-advies voor duurzame groei.</p>
909:                         <ul class="pro-list">
910:                             <li>Architectuur & planning</li>
911:                             <li>Design systems</li>
912:                             <li>Release-strategie</li>
913:                         </ul>
914:                     </div>
915:                 </div>
916:                 <div class="pro-cta">
917:                     <a href="#projects" class="btn">Bekijk projecten</a>
918:                     <a href="#contact" class="btn btn-primary btn-text">Plan een gesprek</a>
919:                 </div>
920:             </div>
921:             <aside class="pro-aside">
922:                 <div class="pro-card">
923:                     <h3>Tech Stack</h3>
924:                     <div class="tech-badges" style="margin-top:0.5rem;">
925:                         <span class="badge">HTML5</span>
926:                         <span class="badge">CSS3</span>
927:                         <span class="badge">JavaScript</span>
928:                         <span class="badge">PHP</span>
929:                         <span class="badge">MySQL</span>
930:                         <span class="badge">C#</span>
931:                     </div>
932:                 </div>
933:                 <div class="metrics">
934:                     <div class="metric">
935:                         <div class="num">3+ jaar</div>
936:                         <div class="lbl">Ervaring</div>
937:                     </div>
938:                     <div class="metric">
939:                         <div class="num">15+</div>
940:                         <div class="lbl">Projecten</div>
941:                     </div>
942:                     <div class="metric">
943:                         <div class="num">100%</div>
944:                         <div class="lbl">Toewijding</div>
945:                     </div>
946:                 </div>
947:             </aside>
948:         </div>
949:     </section>
950: 
951:     <!-- About Section -->
952:     <section class="about" id="about">
953:         <div class="about-constellation" aria-hidden="true">
954:             <svg viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice">
955:                 <g>
956:                     <line class="line" x1="220" y1="160" x2="300" y2="240" />
957:                     <line class="line" x1="300" y1="240" x2="380" y2="200" />
958:                     <line class="line" x1="300" y1="240" x2="320" y2="320" />
959:                     <line class="line" x1="320" y1="320" x2="420" y2="360" />
960:                     <line class="line" x1="420" y1="360" x2="520" y2="300" />
961:                     <line class="line" x1="520" y1="300" x2="600" y2="360" />
962:                     <line class="line" x1="600" y1="360" x2="680" y2="300" />
963:                     <line class="line" x1="680" y1="300" x2="760" y2="360" />
964:                     <line class="line" x1="380" y1="200" x2="460" y2="140" />
965:                     <line class="line" x1="460" y1="140" x2="540" y2="200" />
966:                     <circle class="star" cx="220" cy="160" r="3" />
967:                     <circle class="star" cx="300" cy="240" r="3" />
968:                     <circle class="star" cx="380" cy="200" r="3" />
969:                     <circle class="star" cx="320" cy="320" r="3" />
970:                     <circle class="star" cx="420" cy="360" r="3" />
971:                     <circle class="star" cx="520" cy="300" r="3" />
972:                     <circle class="star" cx="600" cy="360" r="3" />
973:                     <circle class="star" cx="680" cy="300" r="3" />
974:                     <circle class="star" cx="760" cy="360" r="3" />
975:                     <circle class="star" cx="460" cy="140" r="3" />
976:                     <circle class="star" cx="540" cy="200" r="3" />
977:                 </g>
978:                 <g opacity="0.45">
979:                     <circle class="star" cx="100" cy="80" r="2" />
980:                     <circle class="star" cx="180" cy="400" r="2" />
981:                     <circle class="star" cx="980" cy="120" r="2" />
982:                     <circle class="star" cx="850" cy="500" r="2" />
983:                     <circle class="star" cx="1080" cy="420" r="2" />
984:                     <circle class="star" cx="720" cy="100" r="2" />
985:                     <circle class="star" cx="560" cy="520" r="2" />
986:                 </g>
987:             </svg>
988:         </div>
989:         <h2 class="section-title">Ontmoet Colin</h2>
990:         <p class="section-subtitle">Een gepassioneerde ontwikkelaar die graag websites bouwt en digitale oplossingen
991:             creëert.</p>
992:         <div class="about-content">
993:             <div class="about-main-card">
994:                 <div class="about-flex">
995:                     <div class="about-text">
996:                         <div class="subtitle">SOFTWARE DEVELOPER</div>
997:                         <h3>Ik ben Colin Poort</h3>
998:                         <p>Een 18-jarige Software Developer die zich vooral richt op front-end ontwikkeling. Gedreven
999:                             door een echte liefde voor het vak, vind ik vreugde in het bouwen van prachtige websites.
1000:                         </p>
1001:                         <p>Of het nu gaat om de energie van een live applicatie of de subtiele emotie in een
1002:                             gebruikersinterface, ik streef er altijd naar het beste uit elk project te halen.</p>
1003:                         <p>Met ervaring in HTML, CSS, JavaScript, PHP, C# en databases zoals MySQL, bouw ik graag
1004:                             responsieve en gebruiksvriendelijke webapplicaties die echt functioneren.</p>
1005:                         <a href="image/ColinCV.pdf" class="cta-button">Download CV</a>
1006:                     </div>
1007:                     <div class="about-image-wrapper">
1008:                         <div class="about-image">
1009:                             <img src="image/IMG_4909.jpg" alt="Colin Poort">
1010:                         </div>
1011:                     </div>
1012:                 </div>
1013:             </div>
1014:             <div class="about-stats">
1015:                 <div class="stat-card">
1016:                     <div class="stat-number">3+</div>
1017:                     <div class="stat-label">Jaar Ervaring</div>
1018:                 </div>
1019:                 <div class="stat-card">
1020:                     <div class="stat-number">15+</div>
1021:                     <div class="stat-label">Projecten Voltooid</div>
1022:                 </div>
1023:                 <div class="stat-card">
1024:                     <div class="stat-number">100%</div>
1025:                     <div class="stat-label">Passie & Toewijding</div>
1026:                 </div>
1027:             </div>
1028:         </div>
1029:     </section>
1030: 
1031:     <!-- Features Section -->
1032:     <section class="features" id="skills">
1033:         <h2 class="section-title">Wat Maakt Colin Uniek</h2>
1034:         <p class="section-subtitle">Deze eigenschappen maken mij een waardevolle toevoeging aan elk ontwikkelteam</p>
1035:         <div class="features-grid">
1036:             <div class="feature-card">
1037:                 <div class="feature-icon">
1038:                     <img src="image/commitment.png" alt="Toewijding">
1039:                 </div>
1040:                 <h3>Toegewijd</h3>
1041:                 <p>Ik zet me volledig in voor elk project. Elk ontwikkelproject krijgt mijn volledige aandacht waarbij
1042:                     ik streef naar niet alleen code, maar authentieke oplossingen vol functionaliteit.</p>
1043:             </div>
1044:             <div class="feature-card">
1045:                 <div class="feature-icon">
1046:                     <img src="image/innovation.png" alt="Innovatie">
1047:                 </div>
1048:                 <h3>Innovatieve Denker</h3>
1049:                 <p>Ik stuur innovatie aan door het verkennen van moderne frameworks en technologieën. Ik ben altijd op
1050:                     zoek naar nieuwe manieren om uitdagingen aan te pakken.</p>
1051:             </div>
1052:             <div class="feature-card">
1053:                 <div class="feature-icon">
1054:                     <img src="image/problem-solve.png" alt="Probleemoplosser">
1055:                 </div>
1056:                 <h3>Probleemoplosser</h3>
1057:                 <p>Het gaat om het oplossen van problemen, het begrijpen van gebruikersbehoeften en het creëren van
1058:                     oplossingen die echt werken. Ik zet complexe uitdagingen om in eenvoudige oplossingen.</p>
1059:             </div>
1060:         </div>
1061:     </section>
1062: 
1063:     <!-- Projects Section -->
1064:     <section class="projects" id="projects">
1065:         <div class="projects-container">
1066:             <h2 class="section-title">Uitgelichte Projecten</h2>
1067:             <p class="section-subtitle">Een verzameling van mijn beste werk — van interactieve applicaties tot complexe
1068:                 weboplossingen</p>
1069: 
1070:             <!-- Filter buttons -->
1071:             <div class="project-filters">
1072:                 <button class="filter-btn active" data-filter="all"><span>🎯 Alle Projecten</span></button>
1073:                 <button class="filter-btn" data-filter="web"><span>🌐 Web Apps</span></button>
1074:                 <button class="filter-btn" data-filter="game"><span>🎮 Games</span></button>
1075:                 <button class="filter-btn" data-filter="education"><span>📚 Educatie</span></button>
1076:             </div>
1077: 
1078:             <div class="projects-grid">
1079:                 <!-- Featured Project - Fall Game -->
1080:                 <div class="project-card featured" data-category="game">
1081:                     <div class="project-image">
1082:                         <span class="project-status live">Live</span>
1083:                         <img src="image/spongebob.png" alt="Fall Game">
1084:                     </div>
1085:                     <div class="project-content">
1086:                         <h3>Fall Game</h3>
1087:                         <div class="project-meta">
1088:                             <span class="project-meta-item">
1089:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1090:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1091:                                         d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
1092:                                 </svg>
1093:                                 2024
1094:                             </span>
1095:                             <span class="project-meta-item">
1096:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1097:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1098:                                         d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
1099:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1100:                                         d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z">
1101:                                     </path>
1102:                                 </svg>
1103:                                 2.5k+ spelers
1104:                             </span>
1105:                         </div>
1106:                         <p>Een meeslepend interactief vallend-object spel volledig gebouwd met vanilla JavaScript. Bevat
1107:                             geavanceerde physics, collision detection, score tracking en responsive gameplay die soepel
1108:                             werkt op alle apparaten.</p>
1109:                         <div class="project-tech">
1110:                             <span class="tech-tag">JavaScript</span>
1111:                             <span class="tech-tag">Canvas API</span>
1112:                             <span class="tech-tag">Game Physics</span>
1113:                             <span class="tech-tag">Animation</span>
1114:                         </div>
1115:                         <div class="project-footer">
1116:                             <div class="project-links">
1117:                                 <a href="/game" class="project-link primary" target="_blank">
1118:                                     Speel Nu
1119:                                     <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1120:                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1121:                                             d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z">
1122:                                         </path>
1123:                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1124:                                             d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
1125:                                     </svg>
1126:                                 </a>
1127:                             </div>
1128:                         </div>
1129:                     </div>
1130:                 </div>
1131: 
1132:                 <!-- Gastenboek -->
1133:                 <div class="project-card" data-category="web">
1134:                     <div class="project-image">
1135:                         <span class="project-status live">Live</span>
1136:                         <img src="image/gastenboek.jpg" alt="Gastenboek">
1137:                     </div>
1138:                     <div class="project-content">
1139:                         <h3>Gastenboek Applicatie</h3>
1140:                         <div class="project-meta">
1141:                             <span class="project-meta-item">
1142:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1143:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1144:                                         d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
1145:                                 </svg>
1146:                                 2024
1147:                             </span>
1148:                             <span class="project-meta-item">
1149:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1150:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1151:                                         d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z">
1152:                                     </path>
1153:                                 </svg>
1154:                                 500+ berichten
1155:                             </span>
1156:                         </div>
1157:                         <p>Moderne gastenboek waar bezoekers berichten kunnen achterlaten. Inclusief real-time
1158:                             validatie, spam protectie en elegante UI.</p>
1159:                         <div class="project-tech">
1160:                             <span class="tech-tag">PHP</span>
1161:                             <span class="tech-tag">JSON</span>
1162:                             <span class="tech-tag">JavaScript</span>
1163:                             <span class="tech-tag">CSS3</span>
1164:                         </div>
1165:                         <div class="project-footer">
1166:                             <div class="project-links">
1167:                                 <a href="/gastenboek" class="project-link primary" target="_blank">
1168:                                     Bekijk Live
1169:                                     <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1170:                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1171:                                             d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14">
1172:                                         </path>
1173:                                     </svg>
1174:                                 </a>
1175:                             </div>
1176:                         </div>
1177:                     </div>
1178:                 </div>
1179: 
1180:                 <!-- Gamecraft -->
1181:                 <div class="project-card" data-category="education">
1182:                     <div class="project-image">
1183:                         <span class="project-status live">Live</span>
1184:                         <img src="image/GetImage.png" alt="Gamecraft">
1185:                     </div>
1186:                     <div class="project-content">
1187:                         <h3>Gamecraft Platform</h3>
1188:                         <div class="project-meta">
1189:                             <span class="project-meta-item">
1190:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1191:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1192:                                         d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
1193:                                 </svg>
1194:                                 2023
1195:                             </span>
1196:                             <span class="project-meta-item">
1197:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1198:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1199:                                         d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253">
1200:                                     </path>
1201:                                 </svg>
1202:                                 Educatief
1203:                             </span>
1204:                         </div>
1205:                         <p>Educatief platform met interactieve lessen voor web development. Bevat tutorials, code
1206:                             challenges en live previews.</p>
1207:                         <div class="project-tech">
1208:                             <span class="tech-tag">HTML5</span>
1209:                             <span class="tech-tag">CSS3</span>
1210:                             <span class="tech-tag">JavaScript</span>
1211:                             <span class="tech-tag">Interactive</span>
1212:                         </div>
1213:                         <div class="project-footer">
1214:                             <div class="project-links">
1215:                                 <a href="/gamecraft/html/" class="project-link primary" target="_blank">
1216:                                     Ontdek Platform
1217:                                     <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1218:                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1219:                                             d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
1220:                                     </svg>
1221:                                 </a>
1222:                             </div>
1223:                         </div>
1224:                     </div>
1225:                 </div>
1226: 
1227:                 <!-- Ergowijzer -->
1228:                 <div class="project-card" data-category="web">
1229:                     <div class="project-image">
1230:                         <span class="project-status live">Live</span>
1231:                         <img src="image/pixlr2.png" alt="Ergowijzer">
1232:                     </div>
1233:                     <div class="project-content">
1234:                         <h3>Ergowijzer</h3>
1235:                         <div class="project-meta">
1236:                             <span class="project-meta-item">
1237:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1238:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1239:                                         d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
1240:                                 </svg>
1241:                                 2023
1242:                             </span>
1243:                             <span class="project-meta-item">
1244:                                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1245:                                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1246:                                         d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z">
1247:                                     </path>
1248:                                 </svg>
1249:                                 Team Project
1250:                             </span>
1251:                         </div>
1252:                         <p>Collaboratief groepsproject voor een ergonomische advieswebsite. Inclusief dynamische content
1253:                             en moderne UI/UX principes.</p>
1254:                         <div class="project-tech">
1255:                             <span class="tech-tag">HTML5</span>
1256:                             <span class="tech-tag">CSS3</span>
1257:                             <span class="tech-tag">JavaScript</span>
1258:                             <span class="tech-tag">Team Work</span>
1259:                         </div>
1260:                         <div class="project-footer">
1261:                             <div class="project-links">
1262:                                 <a href="/l3-pro-3-ergowijzer-dumble" class="project-link primary" target="_blank">
1263:                                     Bekijk Project
1264:                                     <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1265:                                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1266:                                             d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14">
1267:                                         </path>
1268:                                     </svg>
1269:                                 </a>
1270:                             </div>
1271:                         </div>
1272:                     </div>
1273:                 </div>
1274:             </div>
1275: 
1276:             <!-- View More Button -->
1277:             <div class="view-more-container">
1278:                 <a href="#projects" class="view-more-btn">
1279:                     <span>Meer projecten komen eraan!</span>
1280:                     <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
1281:                         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
1282:                             d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
1283:                     </svg>
1284:                 </a>
1285:             </div>
1286:         </div>
1287:     </section>
1288: 
1289:     <!-- CTA Section -->
1290:     <section class="cta-section">
1291:         <div class="cta-content">
1292:             <h2>Laten we iets geweldigs bouwen</h2>
1293:             <p>Webontwikkeling is voor mij meer dan alleen code schrijven. Het gaat om het creëren van ervaringen en
1294:                 verhalen vertellen. Of je nu op zoek bent naar een moderne website, een webapplicatie of een technische
1295:                 oplossing, ik werk graag samen om jouw visie tot leven te brengen.</p>
1296:             <a href="#contact" class="cta-button">
1297:                 Neem Contact Op
1298:                 <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" width="20" height="20">
1299:                     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6">
1300:                     </path>
1301:                 </svg>
1302:             </a>
1303:         </div>
1304:     </section>
1305: 
1306:     <!-- Contact Section -->
1307:     <section class="contact" id="contact">
1308:         <div class="contact-inner">
1309:             <div class="contact-left">
1310:                 <h2 class="section-title">Neem Contact Op</h2>
1311:                 <p class="section-subtitle">Klaar om samen te werken? Laat je gegevens achter of neem direct contact op.
1312:                 </p>
1313:                 <div class="contact-cards">
1314:                     <div class="contact-card">
1315:                         <h4>Email</h4>
1316:                         <p><a href="mailto:colinpoort@hotmail.com">colinpoort@hotmail.com</a></p>
1317:                     </div>
1318:                     <div class="contact-card">
1319:                         <h4>Telefoon</h4>
1320:                         <p><a href="tel:+31628449633">06 2844 9633</a></p>
1321:                     </div>
1322:                     <div class="contact-card">
1323:                         <h4>LinkedIn</h4>
1324:                         <p><a href="https://www.linkedin.com/in/colin-poort-587a7b295/" target="_blank">/colin-poort</a>
1325:                         </p>
1326:                     </div>
1327:                     <div class="contact-card">
1328:                         <h4>Locatie</h4>
1329:                         <p>Bunschoten, NL</p>
1330:                     </div>
1331:                 </div>
1332:             </div>
1333:             <form class="contact-form" action="#" method="POST">
1334:                 <div class="form-row">
1335:                     <div class="input-group">
1336:                         <label for="name">Naam</label>
1337:                         <input id="name" name="name" type="text" class="input" placeholder="Jouw naam" required>
1338:                     </div>
1339:                     <div class="input-group">
1340:                         <label for="email">Email</label>
1341:                         <input id="email" name="email" type="email" class="input" placeholder="jij@voorbeeld.nl"
1342:                             required>
1343:                     </div>
1344:                 </div>
1345:                 <div class="input-group">
1346:                     <label for="subject">Onderwerp</label>
1347:                     <input id="subject" name="subject" type="text" class="input" placeholder="Waarmee kan ik helpen?">
1348:                 </div>
1349:                 <div class="input-group">
1350:                     <label for="message">Bericht</label>
1351:                     <textarea id="message" name="message" class="textarea"
1352:                         placeholder="Vertel kort over je project of vraag" required></textarea>
1353:                 </div>
1354:                 <div class="contact-actions">
1355:                     <span class="note">Ik reageer meestal binnen 1 werkdag.</span>
1356:                     <button type="submit" class="btn btn-primary">Verstuur bericht</button>
1357:                 </div>
1358:             </form>
1359:         </div>
1360:     </section>
1361: 
1362:     <!-- Footer -->
1363:     <footer>
1364:         <div class="footer-content">
1365:             <p>© <span id="year">2024</span> Alle rechten voorbehouden - Colin Poort</p>
1366:             <div class="social-links">
1367:                 <a href="https://www.instagram.com/colin_poort/" target="_blank">
1368:                     <img src="image/instagram.png" alt="Instagram">
1369:                 </a>
1370:                 <a href="https://www.linkedin.com/in/colin-poort-587a7b295/" target="_blank">
1371:                     <img src="image/linkedin.png" alt="LinkedIn">
1372:                 </a>
1373:                 <a href="https://github.com/ColinPoort" target="_blank">
1374:                     <img src="image/github.png" alt="GitHub">
1375:                 </a>
1376:             </div>
1377:         </div>
1378:     </footer>
1379: 
1380:     <script>
1381:         // Smooth scroll animation for sections
1382:         const observerOptions = {
1383:             threshold: 0.1,
1384:             rootMargin: '0px 0px -100px 0px'
1385:         };
1386: 
1387:         const observer = new IntersectionObserver((entries) => {
1388:             entries.forEach(entry => {
1389:                 if (entry.isIntersecting) {
1390:                     entry.target.style.opacity = '1';
1391:                     entry.target.style.transform = 'translateY(0)';
1392:                 }
1393:             });
1394:         }, observerOptions);
1395: 
1396:         document.querySelectorAll('.section-title, .section-subtitle, .about-text, .about-image, .feature-card, .project-card, .cta-content, .contact-card, .contact-form').forEach(el => {
1397:             el.style.opacity = '0';
1398:             el.style.transform = 'translateY(30px)';
1399:             el.style.transition = 'all 0.6s ease';
1400:             observer.observe(el);
1401:         });
1402: 
1403:         // Hero grid zoom-out effect on scroll with scroll locking
1404:         const heroGrid = document.getElementById('heroGrid');
1405:         const heroSection = document.getElementById('home');
1406:         const heroContent = document.querySelector('.hero-content');
1407:         let scrollAccumulator = 0;
1408:         let isZoomComplete = false;
1409:         const maxScroll = 2000; // Scroll distance needed to complete zoom
1410:         const scrollBuffer = 200; // Extra scroll needed after animation completes
1411:         const totalScrollNeeded = maxScroll + scrollBuffer; // 2200 total
1412: 
1413:         console.log('Hero grid element:', heroGrid);
1414:         console.log('Hero section:', heroSection);
1415:         console.log('Hero content:', heroContent);
1416: 
1417:         // Prevent actual page scroll until zoom completes
1418:         window.addEventListener('wheel', (e) => {
1419:             // Handle zoom effect when at top of page
1420:             if (window.scrollY < 100) {
1421:                 // Check if scrolling down and not reached buffer limit
1422:                 if (e.deltaY > 0 && scrollAccumulator < totalScrollNeeded) {
1423:                     e.preventDefault();
1424:                     isZoomComplete = false;
1425:                 }
"""
