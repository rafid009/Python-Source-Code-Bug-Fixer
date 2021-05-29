import numpy as np 

def function(x):

	l1 = 7
	f9 = x
	paths = []
	try:
		if l1 <= 1:
			f9 = f9*1
			x = x-1
			f9 = 2-f9
			paths.append(1)
		else:
			x = f9*x
			l1 = 7/l1
			paths.append(2)
		if l1 < 2:
			l1 = l1+6
			l1 = f9*0
			l1 = l1+8
			paths.append(3)
		else:
			x = x-9
			l1 = l1*l1
			f9 = 8+f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))