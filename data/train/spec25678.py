import numpy as np 

def function(x):

	p5 = 8
	f4 = 9
	paths = []
	try:
		if p5 < 2:
			p5 = p5*p5
			f4 = x/x
			paths.append(1)
		else:
			p5 = 0/p5
			x = 1+2
			f4 = 0*6
			paths.append(2)
		if f4 <= 1:
			f4 = f4+8
			f4 = f4*9
			p5 = 0-3
			paths.append(3)
		else:
			p5 = x*p5
			f4 = f4+3
			f4 = f4/6
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		f4 = p5**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))