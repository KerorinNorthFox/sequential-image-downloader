from rules.id_required_rule import IdRequiredRule

class WebArchiveOrgRule(IdRequiredRule):
    def __init__(self):
        super().__init__(
            "web.archive.org",
            [],
            start_nth_child_index=0
        )
        
    def get_complete_selectors(self, i: int, uri) -> list[str]:
        for j, dir in enumerate(uri.directories):
            if "http" in dir:
                true_domain = uri.directories[j+1]
        
        from rules.rules import RULES
        for rule in RULES:
            if true_domain == rule():
                true_rule = rule
                
        self._selectors = true_rule.selectors
        self._start_nth_child_index = true_rule.start_nth_child_index
        
        return super().get_complete_selectors(i, uri)
        