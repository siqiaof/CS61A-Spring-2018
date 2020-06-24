(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests) (if (null? rests) (cons (cons first nil) nil) (map (lambda (x) (cons first x)) rests)))

(define (zip pairs)  
  (define (zip-one pairs) (if (null? pairs) () (cons (caar pairs) (zip-one (cdr pairs)))))  
  (define (zip-two pairs) (if (null? pairs) () (cons (car (cdar pairs)) (zip-two (cdr pairs)))))  
  (cons (zip-one pairs) (cons (zip-two pairs) nil))
)	

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (f  n s) (if (null? s) () (cons (cons n (cons (car s) nil)) (f (+ 1 n) (cdr s)))))
  (f 0 s)
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (if (null? denoms) nil
      (if (< total (car denoms)) 
          (list-change total (cdr denoms)) 
          (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms)))))  
)
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr)
        ((quoted? expr)
         (cons 'quote (cdr expr))
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           (cons form (cons params (let-to-lambda body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           (define params (car (zip values)))
           (define vals (cadr (zip values)))
           (cons (cons 'lambda (cons params (let-to-lambda body))) (let-to-lambda vals))
           ))
        (else
         (map let-to-lambda expr)
         )))
