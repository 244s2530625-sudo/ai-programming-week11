# (프로그램 이름을 적으세요)

<!-- 예) 성적 CSV 검증기 -->

<!--
  README 여섯 항목 양식입니다. (실습 PPT 28쪽 · 학습지 ⑤와 같은 순서)
  1. 이 파일의 이름을 README.md 로 바꾼 뒤 아래 칸을 채웁니다.
  2. <!-- 로 시작하는 설명은 다 채운 뒤 지웁니다.
  3. 명령은 직접 실행해 보고, 실제로 나온 결과만 적습니다.
  4. 공개 저장소이므로 학번·연락처는 적지 않습니다. (학번은 학습지에만)
  5. 각 칸의 내용은 설명이 끝나는 줄 아래 빈 줄에 적습니다. (설명 안에 쓰면 GitHub에 보이지 않습니다)

  판정 기준: 처음 보는 사람이 이 문서만 보고 실행과 테스트를 할 수 있는가.
  (게시 후 새 폴더에 clone해 이 문서대로 직접 실행해 봅니다)
-->

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV를 받아 유효한 점수와 제외한 부분을 이유와 함께 돌려준다.

## ② 왜 만들었나요 (Why)

CSV에서 유효 데이터를 구분하고 잘못된 부분은 제외 후 이유를 확인하려고 하였다. 빈 칸, 0~100 범위 밖, 칸 수 틀림, 이름/점수 빈칸, 정수 아님, 파일 없음, 빈 줄, 중복 등의 제외 이유가 있음. 

## ③ 어떻게 쓰나요 (How)

읽은 줄 : 5개
  김하나 88
  최,네번 77
  김하나 91
  윤보람 64
  서한별 95
건너뛴 줄 : 5개
  3행  이두리,105   ← 점수가 0~100 밖
  4행  박세찬,   ← 점수가 비어 있음
  7행  정오름,-5   ← 점수가 0~100 밖
  8행  한겨울,결석   ← 점수가 정수가 아님
  9행  장미르,72,비고없음   ← 열 개수가 2가 아님
13 passed in 0.08s

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv
```


예상 결과: ( 읽은 줄 5개 / 건너뛴 줄 5개)

## ④ 어떻게 테스트하나요

```
python -m pytest test_load_scores.py -q
```

실제 결과: ( 13 passed in 0.11s)



## ⑤ 파일 구성

| load_scores.py | CSV를 읽어 (kept, skipped)를 돌려주는 함수 |
| scores.csv | 성적 데이터가 들어 있는 CSV 파일 |
| empty.csv | 헤더만 들어 있는 CSV 파일 |
| weird.csv | 다양한 잘못된 입력이 들어 있는 CSV 파일 |
| bug3_logic.py | find_max와 count_pass 함수가 들어 있는 파일 |
| prompts.txt | 실습에서 사용할 AI 요청문이 들어 있는 파일 |
| README_양식.md | README 작성 양식 파일 |
| LICENSE | 프로그램의 라이선스 파일 |
| .gitignore | Git에서 제외할 파일과 폴더를 지정하는 파일 |
| test_bug_A.py | find_max를 검사하는 실험 2-A 테스트 파일 |
| test_bug_B.py | find_max를 검사하는 실험 2-B 테스트 파일 |
| test_load_scores.py | load_scores를 검사하는 테스트 파일 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : 조용준
- 사용한 AI 도구·모델 : VS Code Copilot Chat (Ask)
- AI에게 도움받은 부분 : 파일구성
- 내가 직접 판단·확인한 부분 : 무엇을 하나요, 왜 만들었나요, 어떻게 쓰나요, 어떻게 테스트하나요

## 라이선스

MIT License (LICENSE 파일 참고)
Copyright (c) 2026 (조용준)
