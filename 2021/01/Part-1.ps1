<#
    Advent of Code

    --- Day 1: Sonar Sweep ---
    Link: https://adventofcode.com/2021/day/1

    --- Part One ---
    The first order of business is to figure out how quickly the depth increases, 
    just so you know what you're dealing with
    you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

    To do this, count the number of times a depth measurement increases from the previous measurement. 
    (There is no measurement before the first measurement.)
#>

[CmdletBinding()]
Param ()

$data = get-content '.\input.txt'
$DepthIncreased = 0
$PreviousMeasurement = 0

for ($i=0; $i -lt $Data.Count; $i++) {
    $CurrentMeasurement = $data[$i]

    # Skip the fist measurement
    if ($i -eq 0) {
        Write-Verbose "$CurrentMeasurement (N/A - no previous measurement)"
    }

    # Check how the current measurement diffir from the previus
    if ($CurrentMeasurement -gt $PreviousMeasurement) {
        Write-Verbose "$CurrentMeasurement (increased)"
        $DepthIncreased++
    }
    else {
        Write-Verbose "$CurrentMeasurement (decreased)"
    }
    
    $PreviousMeasurement = $CurrentMeasurement
}

Write-Verbose "Result: $($DepthIncreased)"
return $DepthIncreased