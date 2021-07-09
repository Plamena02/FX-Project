
$key_file = "C:\Users\User\Desktop\FX Project\forex_pairs.csv"
$output_file = "C:\Users\User\Desktop\FX Project\output.csv"

#If the file does not exist, create it.
if (-not(Test-Path -Path $output_file -PathType Leaf)) {
     try {
         $null = New-Item -ItemType File -Path $file -Force -ErrorAction Stop
         Write-Host "The file [$output_file] has been created."
     }
     catch {
         throw $_.Exception.Message
     }
    }
    # If the file already exists, show the message and clear the old file.
    else {
        Clear-Content "C:\Users\User\Desktop\FX Project\output.csv"
        Write-Host "Cannot create [$output_file] because a file with that name already exists."
    }

    #Read input currency document 
    $lines = Get-Content -Path $key_file  

    #Start and End date (5 days)
    [datetime]$date = (Get-Date).AddDays(-5)
    $period1 = [int](Get-Date -Date $date -UFormat %s -Millisecond 0)
    $period2 = [int](Get-Date -UFormat %s -Millisecond 0)

    #Create new folder for download files
    New-Item -Path 'C:\Users\User\Desktop\FX Project\Data' -ItemType Directory
    $path = "C:\Users\User\Desktop\FX Project\Data"

    foreach($line in $lines) 
    {
        $arr = $line.Split(",")
        if ($arr[0] -ne "from") 
        {
            if($arr[0] -eq "USD")
            {        
                $currency = $arr[1] + "=X"
            }
            else 
            {
                $currency = $arr[0]+ $arr[1] + "=X"
            }
            
            $index = $arr[2]
            $params = @{
                    'export' = '1'
                    'enc'    = 'UTF-8'
                    'xf'     = 'cs'
            }

            try {
                Invoke-WebRequest -Uri "https://query1.finance.yahoo.com/v7/finance/download/${currency}?period1=${period1}&period2=${period2}&interval=1d&events=history&includeAdjustedClose=true" -Body $params -OutFile $path\$index.csv 
            }
            catch {
               Write-Host "The currency $currency was not found."
            }
        }
    }
    
    # Remove-Item 'C:\Users\User\Desktop\FX Project\Data'
    #Add-Content -Path $file -Value $currency