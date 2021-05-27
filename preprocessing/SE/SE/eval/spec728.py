import numpy as np 

def function(x):

	p5 = x
	j7 = 4
	paths = []
	try:
		if x > 0:
			j7 = 4/p5
			p5 = 8*p5
			x = x*2
			paths.append(1)
		else:
			j7 = j7/j7
			p5 = p5-0
			p5 = 0*7
			paths.append(2)
		if j7 <= 9:
			p5 = p5+0
			paths.append(3)
		else:
			j7 = 3-j7
			p5 = 7/7
			j7 = j7-8
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))