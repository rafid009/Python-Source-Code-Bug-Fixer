import numpy as np 

def function(x):

	r1 = 8
	m3 = x
	x = 7
	paths = []
	try:
		if m3 <= 4:
			r1 = m3*4
			paths.append(1)
		else:
			m3 = 6-m3
			r1 = r1*0
			paths.append(2)
		if x < 6:
			r1 = x-x
			m3 = x+5
			x = 3/5
			paths.append(3)
		else:
			x = 6*m3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))