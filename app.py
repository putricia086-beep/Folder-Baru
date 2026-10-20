import streamlit as st

st.set_page_config(
    page_title="Cargo Drone Project",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        html {
            scroll-behavior: smooth;
        }

        body {
            background: #f3f6fb;
            color: #132431;
            font-family: 'Inter', sans-serif;
        }

        [data-testid="stAppViewContainer"] {
            background: #f3f6fb;
            color: #132431;
        }

        .main .block-container {
            max-width: 1180px;
            padding-top: 1.2rem;
            padding-bottom: 3rem;
        }

        .site-shell {
            background: #f3f6fb;
            color: #132431;
        }

        .topbar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(15, 23, 42, 0.08);
            padding: 0.9rem 0;
            margin: 0 -1rem 1.3rem -1rem;
        }

        .topbar-inner {
            max-width: 1180px;
            margin: 0 auto;
            padding: 0 1.2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.04em;
        }

        .brand-mark {
            width: 2.4rem;
            height: 2.4rem;
            border-radius: 0.8rem;
            background: linear-gradient(135deg, #1e5eff, #5ad7c5);
            color: white;
            display: grid;
            place-items: center;
            font-size: 0.88rem;
        }

        .nav {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .nav a {
            color: #475569;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            padding: 0.5rem 0.8rem;
            border-radius: 999px;
            transition: all 0.2s ease;
        }

        .nav a:hover {
            background: #eaf1ff;
            color: #0f172a;
        }

        .btn-row {
            display: flex;
            gap: 0.9rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }

        .primary-btn, .ghost-btn {
            display: inline-block;
            text-decoration: none;
            border-radius: 999px;
            padding: 0.8rem 1.3rem;
            font-weight: 700;
            transition: all 0.2s ease;
            border: 1px solid transparent;
        }

        .primary-btn {
            background: linear-gradient(135deg, #1e5eff, #5ad7c5);
            color: white;
            box-shadow: 0 12px 24px rgba(30, 94, 255, 0.18);
        }

        .ghost-btn {
            background: white;
            border-color: rgba(15, 23, 42, 0.08);
            color: #0f172a;
        }

        .hero {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 1.5rem;
            align-items: center;
            padding: 2rem 0 1rem 0;
        }

        .eyebrow {
            color: #0c6bff;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            font-size: 0.7rem;
            font-weight: 800;
            margin: 0 0 1rem 0;
        }

        .hero h1 {
            margin: 0;
            font-size: clamp(2.4rem, 5vw, 4.2rem);
            line-height: 1.06;
            letter-spacing: -0.06em;
            color: #0f172a;
        }

        .lead {
            margin-top: 1rem;
            font-size: 1.07rem;
            line-height: 1.8;
            color: #475569;
            max-width: 700px;
        }

        .stats {
            margin-top: 1.5rem;
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
        }

        .stat {
            background: white;
            border: 1px solid rgba(15, 23, 42, 0.06);
            border-radius: 1rem;
            padding: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.03);
        }

        .stat strong {
            display: block;
            font-size: 1.05rem;
            color: #111827;
            margin-bottom: 0.25rem;
        }

        .stat span {
            color: #64748b;
            font-size: 0.78rem;
        }

        .visual-card {
            background: linear-gradient(135deg, #eaf3ff, #eefdf8);
            border: 1px solid rgba(15, 23, 42, 0.06);
            border-radius: 1.6rem;
            padding: 1.5rem;
            min-height: 470px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 18px 50px rgba(15, 23, 42, 0.08);
        }

        .visual-card::before,
        .visual-card::after {
            content: "";
            position: absolute;
            border-radius: 50%;
            filter: blur(28px);
        }

        .visual-card::before {
            width: 220px;
            height: 220px;
            background: rgba(30, 94, 255, 0.12);
            left: 40px;
            top: 48px;
        }

        .visual-card::after {
            width: 240px;
            height: 240px;
            background: rgba(90, 215, 197, 0.14);
            right: 30px;
            bottom: 25px;
        }

        .drone-svg {
            width: 320px;
            height: 320px;
            position: relative;
            z-index: 1;
        }

        .section {
            padding: 3.5rem 0;
            scroll-margin-top: 100px;
        }

        .section-head {
            margin-bottom: 1.4rem;
        }

        .section-label {
            color: #0c6bff;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            font-size: 0.7rem;
            font-weight: 800;
            margin-bottom: 0.7rem;
        }

        .section h2 {
            margin: 0;
            color: #0f172a;
            letter-spacing: -0.05em;
            font-size: clamp(1.8rem, 3vw, 2.7rem);
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 1.4rem;
            align-items: start;
        }

        .card {
            background: white;
            border: 1px solid rgba(15, 23, 42, 0.06);
            border-radius: 1.2rem;
            padding: 1.3rem;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.04);
        }

        .muted {
            color: #64748b;
            line-height: 1.8;
        }

        .info-list {
            display: grid;
            gap: 0.9rem;
        }

        .num-badge {
            display: inline-grid;
            place-items: center;
            width: 2.4rem;
            height: 2.4rem;
            border-radius: 0.8rem;
            font-weight: 800;
            background: #edf4ff;
            color: #1451d7;
            margin-bottom: 0.8rem;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
        }

        .grid-2-small {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 1rem;
        }

        .mini-title {
            margin: 0 0 0.6rem;
            color: #0f172a;
            font-size: 1.15rem;
        }

        .list-default {
            margin: 0;
            padding-left: 1.1rem;
            color: #475569;
            line-height: 1.9;
        }

        .simple-footer {
            margin-top: 2rem;
            background: #0f172a;
            border-radius: 1.4rem;
            padding: 1.3rem 1.5rem;
            color: #e2e8f0;
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .simple-footer strong {
            color: white;
        }

        @media (max-width: 900px) {
            .hero, .grid-2, .grid-3, .grid-2-small {
                grid-template-columns: 1fr;
            }

            .nav {
                justify-content: flex-start;
            }
        }
    </style>
    """
)

st.markdown(
    """
    <div class='site-shell'>
        <div class='topbar'>
            <div class='topbar-inner'>
                <div class='brand'>
                    <span class='brand-mark'>CD</span>
                    <span>Cargo Drone</span>
                </div>
                <div class='nav'>
                    <a href="#beranda">Beranda</a>
                    <a href="#tentang">Tentang</a>
                    <a href="#sistem">Sistem</a>
                    <a href="#teknologi">Teknologi</a>
                    <a href="#uji">Uji Coba</a>
                </div>
            </div>
        </div>

        <div id='beranda' class='hero'>
            <div>
                <div class='eyebrow'>Project STI • Sistem & Teknologi Informasi</div>
                <h1>Perancangan &amp; Pembuatan Drone Pengangkut Barang</h1>
                <div class='lead'>
                    Pengembangan sistem drone pengangkut barang berbasis otomatisasi, sensor,
                    dan teknologi informasi untuk mendukung distribusi barang yang cepat,
                    efisien, dan aman di area tertentu.
                </div>
                <div class='btn-row'>
                    <a href="#tentang" class='primary-btn'>Lihat Detail</a>
                    <a href="#teknologi" class='ghost-btn'>Teknologi</a>
                </div>
                <div class='stats'>
                    <div class='stat'>
                        <strong>Autopilot</strong>
                        <span>Kontrol jarak jauh &amp; otomatis</span>
                    </div>
                    <div class='stat'>
                        <strong>Monitoring</strong>
                        <span>Data real-time via telemetry</span>
                    </div>
                    <div class='stat'>
                        <strong>Payload</strong>
                        <span>Barang ringan hingga menengah</span>
                    </div>
                </div>
            </div>

            <div class='visual-card'>
                <svg class='drone-svg' viewBox='0 0 320 320' xmlns='http://www.w3.org/2000/svg'>
                    <g transform='rotate(12 160 160)'>
                        <g>
                            <rect x='108' y='126' width='104' height='68' rx='18' fill='rgba(20,81,215,0.85)' stroke='rgba(15,23,42,0.2)'/>
                            <rect x='132' y='98' width='56' height='134' rx='18' fill='rgba(30,94,255,0.12)' stroke='rgba(15,23,42,0.15)'/>
                        </g>
                        <g>
                            <rect x='86' y='98' width='90' height='8' rx='4' fill='rgba(15,23,42,0.35)' transform='rotate(45 131 102)'/>
                            <rect x='144' y='98' width='90' height='8' rx='4' fill='rgba(15,23,42,0.35)' transform='rotate(-45 189 102)'/>
                            <rect x='86' y='214' width='90' height='8' rx='4' fill='rgba(15,23,42,0.35)' transform='rotate(-45 131 218)'/>
                            <rect x='144' y='214' width='90' height='8' rx='4' fill='rgba(15,23,42,0.35)' transform='rotate(45 189 218)'/>
                        </g>
                        <g>
                            <circle cx='52' cy='52' r='22' fill='rgba(15,23,42,0.95)' stroke='rgba(255,255,255,0.3)'/>
                            <circle cx='268' cy='52' r='22' fill='rgba(15,23,42,0.95)' stroke='rgba(255,255,255,0.3)'/>
                            <circle cx='52' cy='268' r='22' fill='rgba(15,23,42,0.95)' stroke='rgba(255,255,255,0.3)'/>
                            <circle cx='268' cy='268' r='22' fill='rgba(15,23,42,0.95)' stroke='rgba(255,255,255,0.3)'/>
                        </g>
                        <g stroke='rgba(15,23,42,0.65)' stroke-width='2'>
                            <line x1='52' y1='52' x2='52' y2='76'/>
                            <line x1='52' y1='52' x2='76' y2='52'/>
                            <line x1='268' y1='52' x2='268' y2='76'/>
                            <line x1='268' y1='52' x2='244' y2='52'/>
                            <line x1='52' y1='268' x2='52' y2='244'/>
                            <line x1='52' y1='268' x2='76' y2='268'/>
                            <line x1='268' y1='268' x2='268' y2='244'/>
                            <line x1='268' y1='268' x2='244' y2='268'/>
                        </g>
                    </g>
                </svg>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div id='tentang' class='section'>
        <div class='section-head'>
            <div class='section-label'>Tentang project</div>
            <h2>Fokus Sistem dan Teknologi Informasi</h2>
        </div>
        <div class='grid-2'>
            <div class='card'>
                <p class='muted'>
                    Proyek ini tidak hanya berfokus pada perakitan drone, tetapi juga pada pengembangan
                    sistem informasi yang mengintegrasikan kontrol, navigasi, monitoring, dan analisis data.
                    Dengan pendekatan STI, kami merancang bagaimana drone dapat bekerja secara otomatis,
                    aman, dan terukur dalam pengiriman barang.
                </p>
                <p class='muted'>
                    Bagian STI mencakup sistem pengumpulan data dari sensor, pemrosesan data navigasi,
                    algoritma kontrol, antarmuka monitoring, serta integrasi perangkat lunak yang memungkinkan
                    pengelolaan misi drone secara real-time.
                </p>
            </div>
            <div class='info-list'>
                <div class='card'>
                    <div class='num-badge'>01</div>
                    <h3 class='mini-title'>Monitoring Real-Time</h3>
                    <div class='muted'>Visualisasi posisi, ketinggian, kecepatan, dan status baterai.</div>
                </div>
                <div class='card'>
                    <div class='num-badge'>02</div>
                    <h3 class='mini-title'>Kontrol Misi</h3>
                    <div class='muted'>Perencanaan jalur, koordinat tujuan, dan eksekusi otomatis.</div>
                </div>
                <div class='card'>
                    <div class='num-badge'>03</div>
                    <h3 class='mini-title'>Integrasi Sensor</h3>
                    <div class='muted'>GPS, IMU, ESC, dan sistem komunikasi untuk keamanan terbang.</div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div id='sistem' class='section'>
        <div class='section-head'>
            <div class='section-label'>Arsitektur sistem</div>
            <h2>Bagaimana sistem cargo drone bekerja</h2>
        </div>
        <div class='grid-3'>
            <div class='card'>
                <div class='num-badge'>01</div>
                <h3 class='mini-title'>Input &amp; Sensor</h3>
                <div class='muted'>GPS, IMU, barometer, kamera, dan sensor pendukung untuk posisi serta kestabilan terbang.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>02</div>
                <h3 class='mini-title'>Kontrol Navigasi</h3>
                <div class='muted'>Pengolahan data navigasi dan perencanaan rute untuk mencapai target secara akurat.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>03</div>
                <h3 class='mini-title'>Flight Controller</h3>
                <div class='muted'>Komponen utama yang mengolah sinyal kendali dan menjaga kestabilan drone saat terbang.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>04</div>
                <h3 class='mini-title'>Payload &amp; Delivery</h3>
                <div class='muted'>Modul pengangkut barang yang dapat menahan beban ringan dengan distribusi yang aman.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>05</div>
                <h3 class='mini-title'>Telemetry</h3>
                <div class='muted'>Pengiriman data ke ground station agar operator dapat memantau kondisi drone secara real-time.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>06</div>
                <h3 class='mini-title'>Monitoring UI</h3>
                <div class='muted'>Antarmuka digital untuk status baterai, rute, kondisi terbang, dan log aktivitas.</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div id='teknologi' class='section'>
        <div class='section-head'>
            <div class='section-label'>Teknologi yang digunakan</div>
            <h2>Stack teknologi untuk sistem cargo drone</h2>
        </div>
        <div class='grid-3'>
            <div class='card'>
                <h3 class='mini-title'>Perangkat keras</h3>
                <ul class='list-default'>
                    <li>Flight controller</li>
                    <li>ESC dan motor brushless</li>
                    <li>GPS dan IMU</li>
                    <li>Telemetry radio</li>
                    <li>Battery management system</li>
                    <li>Frame dan payload bay</li>
                </ul>
            </div>
            <div class='card'>
                <h3 class='mini-title'>Perangkat lunak</h3>
                <ul class='list-default'>
                    <li>Sistem kontrol dan navigasi</li>
                    <li>Perancangan misi otomatis</li>
                    <li>Monitoring kondisi drone</li>
                    <li>Analisis data kinerja</li>
                    <li>Interaksi manusia-komputer</li>
                    <li>Dashboard log dan laporan</li>
                </ul>
            </div>
            <div class='card'>
                <h3 class='mini-title'>Fungsi STI</h3>
                <ul class='list-default'>
                    <li>Integrasi sistem sensor dan perangkat</li>
                    <li>Proses data dan keputusan otomatis</li>
                    <li>Desain antarmuka pengguna</li>
                    <li>Pengujian dan validasi sistem</li>
                    <li>Keamanan data dan komunikasi</li>
                    <li>Evaluasi performa &amp; efisiensi</li>
                </ul>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div id='uji' class='section'>
        <div class='section-head'>
            <div class='section-label'>Pengujian &amp; evaluasi</div>
            <h2>Uji coba dilakukan untuk memastikan performa yang optimal</h2>
        </div>
        <div class='grid-2-small'>
            <div class='card'>
                <div class='num-badge'>01</div>
                <h3 class='mini-title'>Uji kestabilan</h3>
                <div class='muted'>Memastikan drone mampu menahan getaran dan menjaga keseimbangan saat terbang.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>02</div>
                <h3 class='mini-title'>Uji navigasi</h3>
                <div class='muted'>Pengujian rute, koordinat tujuan, dan cara drone menyesuaikan jalur secara otomatis.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>03</div>
                <h3 class='mini-title'>Uji muatan</h3>
                <div class='muted'>Mengukur kemampuan drone membawa beban dengan tetap menjaga kestabilan dan daya tahan.</div>
            </div>
            <div class='card'>
                <div class='num-badge'>04</div>
                <h3 class='mini-title'>Uji monitoring</h3>
                <div class='muted'>Analisis status real-time seperti baterai, GPS, ketinggian, dan kondisi sistem.</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='section'>
        <div class='section-head'>
            <div class='section-label'>Manfaat</div>
            <h2>Keunggulan sistem cargo drone</h2>
        </div>
        <div class='grid-3'>
            <div class='card'>
                <h3 class='mini-title'>Efisien</h3>
                <div class='muted'>Mempercepat proses pengiriman barang ke area yang sulit dijangkau.</div>
            </div>
            <div class='card'>
                <h3 class='mini-title'>Aman</h3>
                <div class='muted'>Monitoring dan kontrol sistem membantu meminimalkan risiko kerja.</div>
            </div>
            <div class='card'>
                <h3 class='mini-title'>Terintegrasi</h3>
                <div class='muted'>Gabungan hardware, software, dan data membuat sistem lebih terstruktur.</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='section'>
        <div class='section-head'>
            <div class='section-label'>Tim project</div>
            <h2>Peran STI dalam pengembangan project</h2>
        </div>
        <div class='grid-2'>
            <div class='card'>
                <p class='muted'>
                    Pada bagian STI, kami berperan dalam merancang sistem, mengelola data,
                    menyusun logika kontrol, serta menyajikan antarmuka monitoring dan laporan
                    untuk mendukung keberhasilan penggunaan cargo drone sebagai solusi logistik modern.
                </p>
            </div>
            <div class='card'>
                <div class='muted'>
                    <strong style='color:#0f172a;'>4+</strong><br>
                    Komponen utama sistem
                </div>
                <br>
                <div class='muted'>
                    <strong style='color:#0f172a;'>100%</strong><br>
                    Fokus pada integrasi data dan kontrol
                </div>
                <br>
                <div class='muted'>
                    <strong style='color:#0f172a;'>Realtime</strong><br>
                    Monitoring misi dan performa drone
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='simple-footer'>
        <div>
            <strong>Cargo Drone</strong><br>
            <span style='color:#cbd5e1;'>Project perancangan dan pembuatan drone pengangkut barang dengan pendekatan STI.</span>
        </div>
        <div style='color:#cbd5e1;'>© 2026 Cargo Drone Project</div>
    </div>
    """,
    unsafe_allow_html=True,
)
