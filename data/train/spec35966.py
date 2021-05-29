import numpy as np 

def function(x):

	f3 = x
	p5 = x
	paths = []
	try:
		if f3 >= 8:
			p5 = 5-f3
			paths.append(1)
		else:
			x = x*0
			p5 = 5-4
			paths.append(2)
		if x >= 8:
			x = x+p5
			paths.append(3)
		else:
			x = 9*3
			x = x+2
			f3 = f3*6
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))