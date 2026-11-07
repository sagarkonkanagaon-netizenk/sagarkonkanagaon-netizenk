# Profile assets source

- `reveal.html`: the three.js 3D name reveal behind `assets/banner.webp` (chrome and gold extruded name on a mirror floor, fed by data streams from tech-stack tiles). `font.otf` is Inter Display Black (SIL Open Font License). Serve this folder over HTTP with `three@0.170.0` installed in `node_modules`, then run `node cap.js x 15` to render 150 frames (10 s at 15 fps). Turn the frames into the banner with
  `ffmpeg -framerate 15 -i f/%03d.png -c:v libwebp -q:v 72 -compression_level 6 -loop 0 banner.webp`.
- `gen_svgs.py`: writes every themed SVG in `assets/` (section headers, project cards, lifecycle, principles, toolbox, footer). Run `python3 gen_svgs.py ../assets`.
