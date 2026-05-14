import nbformat as nbf
from nbconvert import NotebookExporter
from nbconvert.preprocessors import TagRemovePreprocessor

def process_and_format_notebook(input_path, output_path_qa, output_path_qp):
    # Load the notebook
    nb = nbf.read(input_path, as_version=4)

    # # Format "question" cells to bold
    # for cell in nb.cells:
    #     if "tags" in cell.metadata and "question" in cell.metadata.tags:
    #         cell.source = "**" + cell.source.strip() + "**"  # Wrap in bold Markdown

    # # Save the formatted notebook temporarily for further processing
    # formatted_path = "temp_formatted_notebook.ipynb"
    # nbf.write(nb, formatted_path)

    # Define processors
    def remove_cells_with_tag(nb, remove_tag):
        preprocessor = TagRemovePreprocessor(remove_cell_tags=[remove_tag], enabled=True)
        exporter = NotebookExporter()

        exporter.register_preprocessor(preprocessor, enabled=True)
        body, _ = exporter.from_notebook_node(nb)
        return nbf.reads(body, as_version=4)

    # Processor 1: Keep "question" + "answer"
    qa_notebook = remove_cells_with_tag(nb, "answer-placeholder")
    nbf.validate(qa_notebook)
    nbf.write(qa_notebook, output_path_qa)

    # # Processor 2: Keep "question" + "answer-placeholder"
    # qp_notebook = remove_cells_with_tag(nb, "answer")
    # nbf.validate(qp_notebook)
    # nbf.write(qp_notebook, output_path_qp)

    print(f"Processed notebooks saved to:\n{output_path_qa}\n{output_path_qp}")

# Define file paths
input_path = "../1b_questions.ipynb"
output_path_qa = "1b_questions_answers.ipynb"
output_path_qp = "1b_questions_questions.ipynb"

# Run the process
process_and_format_notebook(input_path, output_path_qa, output_path_qp)
