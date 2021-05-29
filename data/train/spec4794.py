import numpy as np 

def function(x):

	h2 = x
	q5 = x
	paths = []
	try:
		if x <= 0:
			q5 = h2+0
			q5 = h2*0
			paths.append(1)
		else:
			x = x*2
			q5 = q5+2
			h2 = h2*q5
			paths.append(2)
		if q5 > 1:
			h2 = h2-4
			q5 = q5+8
			q5 = q5-0
			paths.append(3)
		else:
			h2 = h2+h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))