# Thin Windows wrapper over tasks.py — the real task runner.
#
#   .\tasks.ps1 test
#   .\tasks.ps1 verify-all
#   .\tasks.ps1 analyze --clip "L (1).mp4"
#
# Prefers `uv run` so the pinned 3.12 venv is used; falls back to the interpreter
# on PATH if uv is unavailable.
[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$TaskArgs
)

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$Uv = Get-Command uv -ErrorAction SilentlyContinue
if ($Uv) {
    & $Uv.Source run python tasks.py @TaskArgs
} else {
    Write-Warning 'uv not found on PATH — falling back to the active interpreter.'
    & python tasks.py @TaskArgs
}

exit $LASTEXITCODE
