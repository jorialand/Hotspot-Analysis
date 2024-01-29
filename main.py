"""
Hotspot Analysis Tool
@jorialand - 24/01/2023
Focus refactoring on what matters with Hotspots Analysis
https://understandlegacycode.com/blog/focus-refactoring-with-hotspots-analysis/
"""

from pathlib import Path
import subprocess
import pandas as pd
import os
from io import StringIO
import plotly.express as px

def getFileNamesFromPaths(paths: list) -> list:
    return [os.path.basename(path) for path in paths]


def computeComplexity():
    print(computeComplexity.__name__)

    # Using cloc to count lines of code
    # TODO extract complexity computation
    cmdExecutable = Path("C:\\Users\\Horia.Ghionoiu\\Documents\\.discoduro\\Hotspot Analysis\\src\\cloc\\cloc.exe")
    cmdCodebaseDir = Path("C:\\workcopy\\Workstation2\\Alma3D Kernel\\")
    #cmdCodebaseDir = Path("C:\\workcopy\\Workstation2\\")

    # cmdCodebaseDir = Path("C:\\Users\\Horia.Ghionoiu\\Documents\\.discoduro\\Hotspot Analysis\\HotspotAnalysisTestCode")
    cmdParametersByFileByLang = "--by-file-by-lang"
    cmdParametersCsv = "--csv"
    cmdOutFile = "ComplexityByFile.csv"
    cmd = [cmdExecutable.as_posix(), cmdCodebaseDir.as_posix(), cmdParametersByFileByLang, cmdParametersCsv]
    with open(cmdOutFile, "w") as outFile:
        cp = subprocess.run(cmd, stdout=outFile)


    # TODO avoid hardcoded skiprows
    df = pd.read_csv('ComplexityByFile.csv', skiprows=15 , usecols=['language', 'filename', 'blank', 'comment', 'code'], skip_blank_lines=True)
    df = df.rename(columns={'filename': 'path'})
    fileNames = getFileNamesFromPaths(df['path'])
    df.insert(2, 'filename', fileNames)
    df=df[df['language'] == 'C++']
    return df


def computeChurn():
    print(computeChurn.__name__)

    # cp = subprocess.run(["bash", "-c", "./src/ComputeChurn.sh /mnt/c/Users/Horia.Ghionoiu/Documents/.discoduro/Hotspot\ Analysis/HotspotAnalysisTestCode 12"], capture_output=True, text=True)
    cp = subprocess.run(["bash", "-c", "./src/ComputeChurn.sh /mnt/c/workcopy/Workstation2/Alma3D\ Kernel/ 12"], capture_output=True, text=True)
    #cp = subprocess.run(["bash", "-c", "./src/ComputeChurn.sh /mnt/c/workcopy/Workstation2/ 12"], capture_output=True, text=True)

    # print(result.stdout)
    churn = pd.read_csv(StringIO(cp.stdout), sep=';', header=None, names=['churn', 'path'])
    # fileNames = getFileNamesFromPaths(churn['path'])
    # churn.insert(2, 'filename', fileNames)
    churn['path'] = churn['path'].str.replace('/', '\\')
    # churn['path'] = 'C:\\Users\\Horia.Ghionoiu\\Documents\\.discoduro\\Hotspot Analysis\\HotspotAnalysisTestCode\\' + churn['path']
    churn['path'] = 'C:\\workcopy\\Workstation2\\' + churn['path']

    churn = churn[churn['path'].str.endswith('.cpp')]
    # churn = churn[churn['path'].str.contains('\\Poco\\')]
    return churn


def generateGraph(data):
    # print(generateGraph.__name__, " ", "NOT IMPLEMENTED")
    fig = px.scatter(data, x='churn', y='code', hover_name='filename', hover_data={'filename': False})
    fig.update_traces(textposition='top center', marker=dict(size=12, opacity=0.8))
    fig.update_layout(yaxis=dict(autorange='reversed'))
    fig.show()


if __name__ == "__main__":
    complexity = computeComplexity()
    churn = computeChurn()
    # df_complexity_vs_churn = pd.merge(complexity, churn, on='filename')
    complexityChurn = pd.merge(complexity, churn, on='path', how='left')
    generateGraph(complexityChurn)
