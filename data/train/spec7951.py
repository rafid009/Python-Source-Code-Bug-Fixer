import numpy as np 

def function(x):

	p5 = x
	q5 = 7
	paths = []
	try:
		if x > 0:
			x = q5/q5
			x = p5+5
			p5 = p5-q5
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if p5 < 5:
			x = x-x
			p5 = p5/7
			q5 = q5+1
			paths.append(3)
		else:
			p5 = 5+p5
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		q5 = p5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))