# Define SSH parameters
$sshHost = "172.16.0.20"
$sshUser = "your_ssh_username"
$sshPassword = "your_ssh_password" # Or use SSH keys for authentication

# SSH into the server and run the shell script
$session = New-SSHSession -ComputerName $sshHost -Credential (Get-Credential -UserName $sshUser -Password $sshPassword)

if ($session) {
    try {
        # Display a menu
        Write-Host "Select an option:"
        Write-Host "1. Change nginx.conf.test to nginx.conf"
        Write-Host "2. Copy nginx.conf.stream to nginx.conf"
        
        # Read user's choice
        $choice = Read-Host "Enter your choice (1 or 2)"

        # Execute the remote shell script with the user's choice as an argument
        $scriptPath = "/path/to/update_nginx.sh"  # Replace with the actual path
        Invoke-SSHCommand -SSHSession $session -Command "$scriptPath $choice"

    } finally {
        # Close the SSH session
        Remove-SSHSession -SSHSession $session
    }
} else {
    Write-Host "Failed to establish SSH session."
}
