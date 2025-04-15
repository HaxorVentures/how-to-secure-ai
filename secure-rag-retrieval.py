# Filter RAG results based on user permissions in metadata
def filter_retrieved_docs_by_role(retrieved_docs, user_roles):
    """Filters docs where metadata['allowed_roles'] intersects user_roles."""
    allowed_docs = []
    user_roles_set = set(user_roles)
    for doc in retrieved_docs:
        # Assume doc has doc.metadata['allowed_roles'] = ['role1', 'role2']
        doc_roles = set(doc.metadata.get('allowed_roles', []))
        # Allow if doc has no role restrictions OR user has access
        if not doc_roles or user_roles_set.intersection(doc_roles):
            allowed_docs.append(doc)
    return allowed_docs

# --- Usage ---
# user_context = get_user_roles() # e.g., ['dept_A', 'confidential']
# raw_retrieved_docs = vector_db.search(query)
# secure_context_docs = filter_retrieved_docs_by_role(raw_retrieved_docs, user_context)
# # Use ONLY secure_context_docs for LLM prompt
# response = llm.generate(prompt_with(secure_context_docs))