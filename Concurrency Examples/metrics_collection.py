"""
Metrics collection for pipeline observability.
Production pattern: Prometheus metrics for Grafana dashboards.
"""
from dataclasses import dataclass, field
from typing import Dict, List
import time

@dataclass
class PipelineMetrics:
    """Track execution metrics for quality monitoring."""
    task_name: str
    start_time: float = field(default_factory=time.perf_counter)
    end_time: float = 0.0
    attempts: int = 0
    success: bool = False
    error_msg: str = ""
    
    @property
    def duration(self) -> float:
        return round(self.end_time - self.start_time, 4)
    
    def to_dict(self) -> Dict:
        return {
            'task': self.task_name,
            'duration': self.duration,
            'attempts': self.attempts,
            'success': self.success,
            'error': self.error_msg
        }

class MetricsCollector:
    """Aggregate metrics across concurrent tasks."""
    
    def __init__(self):
        self.metrics: List[PipelineMetrics] = []
    
    def add_metric(self, metric: PipelineMetrics) -> None:
        self.metrics.append(metric)
    
    def summary(self) -> Dict:
        """Generate execution summary for monitoring dashboards."""
        if not self.metrics:
            return {}
        
        total_duration = sum(m.duration for m in self.metrics)
        successful = sum(1 for m in self.metrics if m.success)
        total_attempts = sum(m.attempts for m in self.metrics)
        
        return {
            'total_tasks': len(self.metrics),
            'successful': successful,
            'failed': len(self.metrics) - successful,
            'total_duration': round(total_duration, 2),
            'avg_duration': round(total_duration / len(self.metrics), 2),
            'total_attempts': total_attempts,
            'success_rate': round(successful / len(self.metrics) * 100, 2)
        }