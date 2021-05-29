import numpy as np 

def function(x):

	j5 = 7
	p5 = 0
	paths = []
	try:
		if x <= 8:
			p5 = 2-p5
			p5 = 6-p5
			paths.append(1)
		else:
			x = x+3
			x = 6/x
			paths.append(2)
		if p5 > 5:
			x = j5*4
			p5 = p5*0
			j5 = j5+6
			paths.append(3)
		else:
			p5 = j5/4
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))