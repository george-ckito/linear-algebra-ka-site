/* Controls for the offline Manim Slides / Reveal.js export. */
(() => {
  const $ = s => document.querySelector(s);
  let started = false, startTime = 0, generation = 0, presenter = null;
  let finished = false, finishing = false, activeVideo = null;
  let pendingBackEnd = false, backHold = false;
  const PLAYBACK_RATE = 1.3;
  const index = () => Reveal.getIndices().h || 0;
  const elapsed = () => started ? Math.floor((Date.now() - startTime) / 1000) : 0;
  const sync = () => {
    if (presenter && !presenter.closed) presenter.postMessage({type:'lesson-state',index:index(),elapsed:elapsed(),paused:activeVideo?.paused,finished,backHold,started}, '*');
  };
  function update() {
    $('#position').textContent = `${String(index()+1).padStart(2,'0')} / 30`;
    $('#jump').value = index();
    $('#forward').textContent = finished ? 'შემდეგი →' : 'დასრულება →';
    $('#back').disabled = index() === 0;
    $('#forward').disabled = finished && index() === 29;
    sync();
  }
  function cover() {
    $('#loading-frame').src = `openings/${String(index()+1).padStart(2,'0')}.jpg`;
    $('#loading-frame').hidden = false;
  }
  async function seekEnd(video, token) {
    if (!video) return false;
    // Keep the current slide selected even if the user presses during loading.
    for(let i=0; i<600 && token===generation && !Number.isFinite(video.duration); i++)
      await new Promise(r=>setTimeout(r,20));
    if(token!==generation || !Number.isFinite(video.duration)) return false;
    video.pause();
    await new Promise(resolve=>{
      const done=()=>{video.removeEventListener('seeked',done);resolve();};
      video.addEventListener('seeked',done,{once:true});
      video.currentTime=Math.max(0,video.duration-1/60);
      setTimeout(done,1500);
    });
    if(token!==generation) return false;
    video.pause();
    return true;
  }
  async function enter() {
    const token = ++generation;
    const atEnd = pendingBackEnd; pendingBackEnd = false;
    finished = false; finishing = false; activeVideo = null; backHold = false;
    cover(); update();
    // Reveal creates distant background videos lazily.
    for (let tries=0; tries<120 && token===generation; tries++) {
      activeVideo = Reveal.getCurrentSlide()?.slideBackgroundContentElement?.querySelector('video');
      if (activeVideo) break;
      await new Promise(requestAnimationFrame);
    }
    const video = activeVideo;
    if (!video || token !== generation) return;
    video.muted = true; video.playsInline = true; video.loop = false;
    video.playbackRate = PLAYBACK_RATE;
    video.poster = $('#loading-frame').src;
    video.pause();
    try { video.currentTime = 0; } catch {}
    video.onended = () => { if(token!==generation)return; finished=true;finishing=false;backHold=false;update(); };
    video.onerror = () => { if(token===generation)$('#notice').textContent='ვიდეო ვერ გაიხსნა. ZIP სრულად ამოარქივეთ.'; };
    const revealFrame = () => {
      if(token===generation && !finishing) $('#loading-frame').hidden=true;
    };
    if ('requestVideoFrameCallback' in video) video.requestVideoFrameCallback(revealFrame);
    else video.addEventListener('loadeddata',revealFrame,{once:true});
    if (atEnd) {
      // Back navigation lands on the finished state, not the opening state.
      if (await seekEnd(video, token)) {
        finished = true; backHold = true;
        $('#loading-frame').hidden = true; update();
      }
      return;
    }
    if(started) {
      try { await video.play(); } catch(e) {
        if(token===generation && e.name!=='AbortError') $('#notice').textContent='გასაშვებად დააჭირეთ P-ს.';
      }
    }
  }
  function start() {
    started=true;startTime=Date.now();pendingBackEnd=false;backHold=false;$('#welcome').hidden=true;enter();
  }
  async function finish() {
    if (finishing) return;
    finishing = true;
    const token = generation;
    const video = activeVideo;
    if (!(await seekEnd(video, token))) { finishing = false; return; }
    finished = true; finishing = false; backHold = false;
    $('#loading-frame').hidden=true;update();
  }
  function next() {
    if(!started)return start();
    if(finishing)return;
    if(!finished)return finish();
    if(index()<29){backHold=false;Reveal.slide(index()+1);}
  }
  function prev() {
    if(!started)return start();
    // First Back shows the previous scene's finished state. Pressing Back
    // again on that same scene replays it from the beginning.
    if(finished && backHold){backHold=false;enter();return;}
    if(index()>0){pendingBackEnd=true;Reveal.slide(index()-1);}
  }
  function replay(){if(!started)start();else{backHold=false;pendingBackEnd=false;enter();}}
  function toggle(){if(!started)return start();if(finished)return replay();if(!activeVideo)return;activeVideo.paused?activeVideo.play().catch(()=>{}):activeVideo.pause();sync();}
  function jump(n){backHold=false;pendingBackEnd=false;if(!started){started=true;startTime=Date.now();$('#welcome').hidden=true;}if(n===index())enter();else Reveal.slide(n);}
  async function fullscreen(){try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen();}catch{}}
  function notes(){presenter=window.open('presenter.html','linear-algebra-presenter','width=1200,height=850');if(!presenter)$('#notice').textContent='დაუშვით მომხსენებლის ფანჯრის გახსნა ან გამოიყენეთ speaker-notes.html.';else presenter.focus();}
  LESSON.forEach((s,i)=>{const o=document.createElement('option');o.value=i;o.textContent=`${String(i+1).padStart(2,'0')} · ${s.title}`;$('#jump').append(o);});
  $('#start').onclick=start;$('#forward').onclick=next;$('#back').onclick=prev;
  $('#replay').onclick=replay;$('#pause').onclick=toggle;$('#notes').onclick=notes;$('#full').onclick=fullscreen;
  $('#jump').onchange=()=>jump(Number($('#jump').value));
  window.addEventListener('keydown',e=>{
    if(e.target.matches?.('input,select,textarea'))return;
    const key=e.key.toLowerCase();
    const actions={arrowright:next,' ':next,pagedown:next,arrowleft:prev,pageup:prev,r:replay,p:toggle,n:notes,f:fullscreen,home:()=>jump(0),end:()=>jump(29)};
    if(!actions[key])return;
    e.preventDefault();e.stopImmediatePropagation();
    if(!e.repeat)actions[key]();
  },true);
  window.addEventListener('message',e=>{
    if(e.source!==presenter)return;
    if(e.data?.type==='presenter-ready')sync();
    if(e.data?.type==='lesson-command')({next,prev,replay,toggle}[e.data.command]||(()=>{}))();
  });
  Reveal.on('slidechanged',enter);
  Reveal.on('ready',()=>{Reveal.configure({keyboard:false,touch:false,controls:false,transition:'none',backgroundTransition:'none'});enter();});
  setInterval(sync,1000);
  // Read-only state is useful for keyboard regression checks.
  window.lessonState=()=>({index:index(),started,finished,finishing,backHold,time:activeVideo?.currentTime,duration:activeVideo?.duration,paused:activeVideo?.paused,playbackRate:activeVideo?.playbackRate});
})();
