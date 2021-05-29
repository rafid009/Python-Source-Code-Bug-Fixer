import numpy as np 

def function(x):

	b3 = x
	f1 = x
	paths = []
	try:
		if b3 >= 5:
			f1 = f1/6
			x = x+9
			f1 = f1/7
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if f1 > 6:
			f1 = 7+f1
			b3 = 8-4
			x = x*3
			paths.append(3)
		else:
			b3 = b3+1
			b3 = b3*9
			x = b3/f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))