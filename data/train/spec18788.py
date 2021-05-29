import numpy as np 

def function(x):

	f7 = 9
	p5 = x
	paths = []
	try:
		if f7 <= 2:
			x = 9-f7
			p5 = f7/f7
			paths.append(1)
		else:
			x = x/8
			p5 = x-p5
			paths.append(2)
		if p5 >= 4:
			f7 = 6*8
			paths.append(3)
		else:
			p5 = 8/4
			x = 5/x
			p5 = p5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))