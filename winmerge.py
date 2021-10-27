import json
import os
import subprocess


class WinMerge:
    @classmethod
    def output_diff(cls, src_directory: str, dst_directory: str, output_directory_path: str) -> str:
        settings = json.load(
            open('setting\winmerge.json', 'r', encoding='utf-8'))

        outputfile = os.path.join(output_directory_path, 'result.html')

        # WinMergeU.exeのフルパス
        # 比較元ディレクトリのフルパス
        # 比較先ディレクトリのフルパス
        # -minimize：最小化状態でWinMergeを実行する
        # -noninteractive：比較・レポート出力後にWinMergeを終了する
        # -noprefs：レジストリの読み書きはしない
        # -cfg Settings/DirViewExpandSubdirs=1：自動的にサブフォルダを展開する
        # -cfg ReportFiles/ReportType=2：シンプルなHTML形式でレポートを出力する
        # -cfg ReportFiles/IncludeFileCmpReport=1：ファイル比較レポートを含める
        # -r：全てのサブフォルダ内の全てのファイルを比較する
        # -u：比較したパスが「最近使用した項目リスト」に追加されないようにする
        # -or：レポート出力のフルパス
        cmd = f'{settings["winMergePath"]} {src_directory} {dst_directory} -minimize -noninteractive -noprefs -cfg Settings/DirViewExpandSubdirs=1 -cfg ReportFiles/ReportType=2 -cfg ReportFiles/IncludeFileCmpReport=1 -r -u -or {outputfile}'

        print(f'Run WinMerge with the command:{cmd}')
        subprocess.call(cmd)
        print('WinMerge execution is complete.')
        return outputfile
