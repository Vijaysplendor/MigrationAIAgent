from mcp.server.fastmcp import FastMCP
from pipeline_converter import run_pipeline_conversion

mcp = FastMCP("azure-migrator")

@mcp.tool()
def migrate_classic_pipelines(
    input_file: str = "Intial_URL_to_be_converted.txt",
    pat_env_var: str = "ADO_PAT"
) -> dict:
    """
    Migrates classic Azure DevOps pipelines to YAML format.
    """
    try:
        results = run_pipeline_conversion(pat_env_var=pat_env_var, input_file=input_file)
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
if __name__ == "__main__":
    mcp.run()
