import numpy as np 

def function(x):

	p5 = x
	q9 = x
	x = 8
	paths = []
	try:
		if p5 <= 2:
			p5 = 2-p5
			paths.append(1)
		else:
			q9 = p5-q9
			q9 = q9/1
			paths.append(2)
		if p5 < 0:
			p5 = 2+2
			q9 = 7+q9
			q9 = q9-8
			paths.append(3)
		else:
			x = 6/x
			x = 4-1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		p5 = q9**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))