function FetchPipelineIdfromYAML {
    param (
        [Parameter(Mandatory = $True)]
        [String] $resourceType
    )

    $pipelineIdJsonRawUrl = Get-AutomationVariable -Name 'pipelineIdJsonRawUrl'
    $pipelineIdJsonFileContent = Invoke-WebRequest -Uri $pipelineIdJsonRawUrl

    $pipelineIdJson = $pipelineIdJsonFileContent | ConvertFrom-Yaml

    # Write-Host $pipelineIdJsonFileContent

    # Write-Host $resourceType
    foreach ($resource in $pipelineIdJson.resources) {
        if ($resource.resourceType -eq $resourceType) {
            # Write-Host $resource.pipelineID
            # TriggerPipeline -pipelineId $resource.PipelineID -projectName $resource.project
            # Write-Host $resource.pipelineID
            return $resource.pipelineID
        }
    }
}

