<#
    Advent of Code

    --- Day 1: Sonar Sweep ---
    Link: https://adventofcode.com/2021/day/1

    --- Part Two ---
    Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. 
    So, compare A with B, then compare B with C, then C with D, and so on. 
    Stop when there aren't enough measurements left to create a new three-measurement sum.

#>
[CmdletBinding()]
Param ()

$data = get-content '.\input.txt'

$DepthIncreased = 0
$PreviousDataset = 0

for ($i=0; $i-lt $data.Count; $i++) {
    [int]$Dataset = [int]$data[$i] + [int]$data[$i+1] + [int]$data[$i+2]

    # Check if the last part of the data is empty
    if ([int]$Data[$i+2] -eq '') {
        continue
    }

    # Skip the first measurement
    if ($i -eq 0) {
        Write-Verbose "$($Dataset) (N/A - No previous measurement)"
        continue
    }

    # Check how the current measurement diffir from the previus
    if ($Dataset -gt $PreviousDataset) {
        Write-Verbose "$Dataset (increased)"
        $DepthIncreased++
    }
    else {
        Write-Verbose "$Dataset (decreased)"
    }

    $PreviousDataset = $Dataset
}

Write-Verbose "Result: $($DepthIncreased)"
return $DepthIncreased