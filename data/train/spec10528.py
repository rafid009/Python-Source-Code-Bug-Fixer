import numpy as np 

def function(x):

	p2 = 8
	q5 = 5
	paths = []
	try:
		if p2 >= 7:
			q5 = 7/q5
			p2 = p2+4
			paths.append(1)
		else:
			x = x*1
			p2 = 7-p2
			p2 = p2/4
			paths.append(2)
		if q5 <= 6:
			p2 = p2-p2
			paths.append(3)
		else:
			q5 = 5/q5
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))