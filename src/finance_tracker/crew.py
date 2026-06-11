from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class FinanceTracker():
    """FinanceTracker crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def transaction_categorizer(self) -> Agent:
        return Agent(
            config=self.agents_config['transaction_categorizer'],
            verbose=True
        )

    @agent
    def financial_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyzer'],
            verbose=True
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['report_writer'],
            verbose=True
        )

    @agent
    def finance_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['finance_advisor'],
            verbose=True
        )

    @task
    def categorize_task(self) -> Task:
        return Task(
            config=self.tasks_config['categorize_task'],
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task'],
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'],
        )

    @task
    def advise_task(self) -> Task:
        return Task(
            config=self.tasks_config['advise_task'],
            output_file='finance_report.md'   # auto-saves the final output
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FinanceTracker crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )