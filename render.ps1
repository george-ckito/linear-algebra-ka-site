param([switch]$Preview)
$ErrorActionPreference = 'Stop'
$projectPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
$existingPython = Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) 'work\.venv\Scripts\python.exe'
if ((-not (Test-Path -LiteralPath $projectPython)) -and (Test-Path -LiteralPath $existingPython)) {
    & $existingPython -c "import manim, manim_slides; assert manim.__version__ == '0.21.0'" 2>$null
    if ($LASTEXITCODE -eq 0) { $projectPython = $existingPython }
}
if (-not (Test-Path -LiteralPath $projectPython)) {
    py -3 -m venv (Join-Path $PSScriptRoot '.venv')
    if ($LASTEXITCODE -ne 0) { throw 'Python virtual environment creation failed.' }
    & $projectPython -m pip install -r (Join-Path $PSScriptRoot 'requirements.txt')
    if ($LASTEXITCODE -ne 0) { throw 'Manim installation failed.' }
}
& $projectPython (Join-Path $PSScriptRoot 'generate_docs.py')
if ($LASTEXITCODE -ne 0) { throw 'Notes generation failed.' }
if ($Preview) { & $projectPython (Join-Path $PSScriptRoot 'render.py') --height 720 }
else { & $projectPython (Join-Path $PSScriptRoot 'render.py') --height 1080 }
if ($LASTEXITCODE -ne 0) { throw 'Rendering failed. See the preceding error.' }
& $projectPython (Join-Path $PSScriptRoot 'build_presentation.py')
if ($LASTEXITCODE -ne 0) { throw 'Manim Slides export failed.' }
