from flask import Flask, render_template, request
from langgraph import LangGraph
from plan_agent import PlanAgent
from tool_agent import ToolAgent
from reflection import Reflection

app = Flask(__name__)

# Initialize components
lang_graph = LangGraph()
plan_agent = PlanAgent(lang_graph)
tool_agent = ToolAgent(lang_graph)
reflection = Reflection(lang_graph)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_query():
    user_query = request.form['query']
    plan_agent.split_query(user_query)

    results = []
    for task_id in lang_graph.list_tasks().keys():
        result = tool_agent.solve_task(task_id)
        results.append(result)

    feedbacks = []
    for task_id in lang_graph.list_tasks().keys():
        feedback = reflection.reflect_on_task(task_id)
        feedbacks.append(feedback)

    return render_template('result.html', results=results, feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
