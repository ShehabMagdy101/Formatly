# import os
# import json
# import pandas as pd
# import pytest
# from Formatly.src.main import generate_qa_explanation, create_dataset

# # Mock function for testing
# def mock_generate_qa_explanation(text_chunk, is_api=False):
#     return {
#         "question": f"Question about: {text_chunk}",
#         "answer": f"Answer to: {text_chunk}",
#         "explanation": f"Explanation for: {text_chunk}"
#     }

# @pytest.fixture
# def sample_texts():
#     return ["Text A", "Text B", "Text C"]

# def test_generate_qa_explanation_valid(sample_texts, monkeypatch):
#     monkeypatch.setattr("src.main.generate_qa_explanation", mock_generate_qa_explanation)
#     result = generate_qa_explanation(sample_texts[0])
#     assert "question" in result
#     assert "answer" in result
#     assert "explanation" in result

# def test_create_dataset_csv(tmp_path, sample_texts, monkeypatch):
#     monkeypatch.setattr("src.main.generate_qa_explanation", mock_generate_qa_explanation)
#     output_file = tmp_path / "test_dataset.csv"
#     df = create_dataset(sample_texts, format="csv", filename=str(output_file.name))
#     assert not df.empty
#     assert all(col in df.columns for col in ["question", "answer", "explanation"])
#     assert df.isnull().sum().sum() == 0

# def test_create_dataset_invalid_json(monkeypatch):
#     def bad_json_generator(_):
#         return {"question": None, "answer": None, "explanation": None}
#     monkeypatch.setattr("src.main.generate_qa_explanation", bad_json_generator)
#     df = create_dataset(["Bad data"])
#     assert df.empty or df.isnull().any().any()

# def test_export_formats(monkeypatch, sample_texts):
#     monkeypatch.setattr("src.main.generate_qa_explanation", mock_generate_qa_explanation)
#     df = create_dataset(sample_texts, format="chatml")
#     assert not df.empty
