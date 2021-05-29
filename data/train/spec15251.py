import numpy as np 

def function(x):

	f2 = 0
	y7 = 2
	paths = []
	try:
		if f2 <= 9:
			y7 = y7+x
			y7 = y7-7
			f2 = f2-x
			paths.append(1)
		else:
			y7 = y7*6
			f2 = 2+f2
			x = f2*0
			paths.append(2)
		if x < 1:
			x = x+2
			x = x*5
			paths.append(3)
		else:
			f2 = 8-f2
			f2 = y7*6
			f2 = f2/8
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		y7 = f2**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))