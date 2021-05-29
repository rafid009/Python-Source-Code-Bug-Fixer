import numpy as np 

def function(x):

	p5 = x
	v2 = x
	paths = []
	try:
		if v2 >= 9:
			v2 = 1*v2
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if v2 >= 0:
			v2 = 5-v2
			x = x+7
			x = x/8
			paths.append(3)
		else:
			v2 = v2-x
			p5 = p5*p5
			x = 2+8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		p5 = v2**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))