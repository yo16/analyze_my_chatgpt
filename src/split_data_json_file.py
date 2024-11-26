import json
import os
from datetime import datetime


# conversationファイルをchunk_sizeで分割する
def split_data_json_file(input_file, output_dir, chunk_size=20):
    # 出力フォルダ
    current_dt = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"{output_dir}/result_{current_dt}"
    os.makedirs(output_dir, exist_ok=True)

    # JSONをパース
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # データを分割して保存
    for i in range(0, len(data), chunk_size):
        chunk = data[i: i+chunk_size]
        output_file = os.path.join(output_dir, f'conversations_{i // chunk_size + 1}.json')
        with open(output_file, 'w', encoding='utf-8') as out_f:
            json.dump(chunk, out_f, ensure_ascii=False, indent=2)



if __name__=="__main__":
    # 入力ファイル
    input_file = "./data/88416ed1b73236f13c7d50ad8240f5fcdf2db5ac4f1ca86abbad47ac7cad5b26-2024-11-26-01-41-23/conversations.json"

    # 出力ディレクトリ
    output_dir = "./output"

    split_data_json_file(input_file, output_dir)

    print("finished")
