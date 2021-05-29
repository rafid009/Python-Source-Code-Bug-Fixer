import numpy as np 

def function(x):

	f4 = x
	p5 = 2
	paths = []
	try:
		if f4 <= 6:
			x = 9+p5
			p5 = 9/p5
			paths.append(1)
		else:
			f4 = 9+9
			paths.append(2)
		if f4 > 2:
			p5 = p5/1
			paths.append(3)
		else:
			f4 = f4/3
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))