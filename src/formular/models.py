from dataclasses import dataclass

@dataclass
class EnvBuildInfoParameter:
    terraformWorkspace: str
    terraformProject: str
    jenkinsServerName: str
    jenkinsJobName: str
    jenkinsJobBranch: str
    envOwner: str