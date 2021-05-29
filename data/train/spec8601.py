import numpy as np 

def function(x):

	m1 = 9
	f1 = 7
	paths = []
	try:
		if m1 >= 9:
			x = 2*x
			f1 = 0-m1
			paths.append(1)
		else:
			m1 = m1+9
			x = 7-x
			x = x-3
			paths.append(2)
		if f1 < 9:
			f1 = f1*9
			m1 = m1/8
			paths.append(3)
		else:
			f1 = f1/5
			f1 = f1-2
			f1 = x*0
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