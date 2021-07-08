
$file1 = "C:\Users\User\Desktop\FX Project\forex_pairs.csv"
$file = "C:\Users\User\Desktop\FX Project\output.csv"
$path = "C:\Users\User\Desktop\FX Project"

# $text = 'Hello World'
# $text >> $file

#If the file does not exist, create it.
if (-not(Test-Path -Path $file -PathType Leaf)) {
     try {
         $null = New-Item -ItemType File -Path $file -Force -ErrorAction Stop
         Write-Host "The file [$file] has been created."
     }
     catch {
         throw $_.Exception.Message
     }
    }
    # If the file already exists, show the message and clear the old file.
    else {
        Clear-Content "C:\Users\User\Desktop\FX Project\output.csv"
        Write-Host "Cannot create [$file] because a file with that name already exists."
    }
    #$lines = Get-Content -Path $file1
    # foreach($line in Get-Content $file1) {
    #     if($line -match $regex){
    #         $line >> $file
    #     }
    # }

    #New-Item -Path 'C:\Users\User\Desktop\FX Project\Data' -ItemType Directory
    #Remove-Item 'C:\Users\User\Desktop\FX Project\Data'

    # $params = @{
    #     'export' = '1'
    #     'enc'    = 'UTF-8'
    #     'xf'     = 'cs'
    # }
    
    # Invoke-WebRequest -Uri "https://query1.finance.yahoo.com/v7/finance/download/ZAC=X?period1=1625184000&period2=1625616000&interval=1d&events=history&includeAdjustedClose=true" -Body $params -OutFile $path\report.csv    