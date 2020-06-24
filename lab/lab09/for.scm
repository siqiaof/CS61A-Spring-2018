(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals)
)