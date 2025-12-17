# gen_recent_md.ps1
$N = 10
$out = "docs/recent.md"

$log = git log --name-only --pretty=format:%ct

$time = 0
$map = @{}

foreach ($line in $log) {
    if ($line -match '^\d+$') {
        $time = [int64]$line
    }
    elseif ($line -match '\.md$' -and $line -notmatch '^docs/library/') {
        if (-not $map.ContainsKey($line)) {
            $map[$line] = $time
        }
    }
}

$map.GetEnumerator() |
Sort-Object Value -Descending |
Select-Object -First $N |
ForEach-Object {
    $date = [DateTimeOffset]::FromUnixTimeSeconds($_.Value).ToLocalTime().ToString("yyyy-MM-dd")
    "- [$($_.Key)]($($_.Key)) - $date"
} | Set-Content $out -Encoding UTF8

# .\gen_recent_md.ps1
