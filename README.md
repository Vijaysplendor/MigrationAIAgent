# MigrationAIAgent
This Repo is used for the migration accelerators to infuse AI by creating an AI Agent that uses MCP server

# End-to-End Architecture

           +-----------------------+
           |   Claude Desktop UI   |
           +----------+------------+
                      |
                      | Calls MCP Tool via function
                      v
         +------------+-------------+
         |  FastMCP Server (Python) |
         +------------+-------------+
                      |
                      | Calls migration script
                      v
       +--------------+----------------+
       | pipeline_converter.py (Logic) |
       +--------------+----------------+
                      |
                      v
     Azure DevOps REST APIs (YAML conversion, Git commit)

# Script Flow Diagram

             Claude Desktop ➝ migrate_classic_pipelines()
                      |
                      v
             +-------------------------+
             | run_pipeline_conversion |
             +-------------------------+
                      |
                      v
               [Loop over each URL]
                      |
                      v
             +------------------------------+
             | get_converted_yaml_content()|
             +------------------------------+
                      |
                      v
             +---------------------------+
             | get_repositories()        |
             +---------------------------+
                      |
                      v
             +----------------------------+
             | get_latest_commit()       |
             +----------------------------+
                      |
                      v
             +----------------------------------+
             | create_branch_with_yaml()        |
             +----------------------------------+

# Simplified Sequence diagram

Claude Desktop Role : Claude Desktop acts as a frontend

           Claude Desktop
                |
                | migrate_classic_pipelines()
                |
           FastMCP Tool (azure_mcp_tool.py)
                |
                | run_pipeline_conversion()
                |
           pipeline_converter.py
                |
           Azure DevOps API



