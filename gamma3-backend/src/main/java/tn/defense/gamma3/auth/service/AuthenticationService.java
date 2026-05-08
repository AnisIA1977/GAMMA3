package tn.defense.gamma3.auth.service;

import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import tn.defense.gamma3.auth.api.dto.AuthDto;
import tn.defense.gamma3.auth.domain.User;
import tn.defense.gamma3.auth.repository.UserRepository;

@Service
@RequiredArgsConstructor
public class AuthenticationService {

    private final UserRepository repository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    public AuthDto.AuthResponse register(AuthDto.RegisterRequest request) {
        var user = User.builder()
                .matricule(request.getMatricule())
                .fullName(request.getFullName())
                .password(passwordEncoder.encode(request.getPassword()))
                .role(request.getRole())
                .build();
        repository.save(user);
        var jwtToken = jwtService.generateToken(user);
        return AuthDto.AuthResponse.builder()
                .token(jwtToken)
                .matricule(user.getMatricule())
                .fullName(user.getFullName())
                .role(user.getRole())
                .build();
    }

    public AuthDto.AuthResponse authenticate(AuthDto.LoginRequest request) {
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        request.getMatricule(),
                        request.getPassword()
                )
        );
        var user = repository.findByMatricule(request.getMatricule())
                .orElseThrow(); // Devrait pas arriver si l'auth réussit
        var jwtToken = jwtService.generateToken(user);
        return AuthDto.AuthResponse.builder()
                .token(jwtToken)
                .matricule(user.getMatricule())
                .fullName(user.getFullName())
                .role(user.getRole())
                .build();
    }
}
