<h1 align="center">mimcvdf ⏲️</h1>

<p align="center"><i>Simple <a href="https://eprint.iacr.org/2018/601.pdf">Verifiable Delay Function<a> using <a href="https://eprint.iacr.org/2016/492.pdf">MiMC</a></i></p>

## Applications

This module was created for use in reducing spam in a similar manner to [HashCash](https://en.wikipedia.org/wiki/Hashcash). However, some potential uses for VDFs include blockchains and verifiable lotteries.


## Security


This code has not been audited for security. It is not currently recommended for protecting against anything but denial of service, even though MiMC is able to do much more. If used, make sure it is not protecting anything critical.

In addition, since this is a Python implementation, attackers can be faster than typical users of an application by using faster language implementations or even FPGAs.

