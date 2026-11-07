# Profile assets source

- `gauntlet.html`: the three.js scene behind `assets/banner.webp`. An armored data gauntlet snaps, then the holographic data world builds and plays out (12 s). Serve this folder over HTTP with `three@0.170.0` in `node_modules`, run `node capx.js gauntlet.html f fps:15:12 3200`, then
  `ffmpeg -framerate 15 -i f/%03d.png -vf scale=2400:600:flags=lanczos -c:v libwebp -q:v 75 -compression_level 6 -loop 0 banner.webp` (renders at 3200×800, downsampled to 2400×600 for crisp edges under 10 MB).

- `hero.html`: the previous ray-traced data-hero banner scene, with HTML overlays for the headline and HUD panels. Serve this folder over HTTP with `three@0.170.0` installed in `node_modules`, then run `node cap.js 0 f x 15` to render 150 frames (10 s at 15 fps). Turn the frames into the banner with
  `ffmpeg -framerate 15 -i f/%03d.png -c:v libwebp -q:v 72 -compression_level 6 -loop 0 banner.webp`.
- `gen_svgs.py`: writes every themed SVG in `assets/` (section headers, project cards, lifecycle, principles, toolbox, footer). Run `python3 gen_svgs.py ../assets`.
